#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'levitan'

"""
This is matrix release for 1D quantum walk with different shift simulation(graph).
基本过程：有一个初始量子态，coin是一个幺正变换，一次游走即coin对量子态变换一次
然后根据量子态walk一步，或几步（根据shift而定）得到一个位置概率分布，如此反复。
"""

from numpy import *
from matplotlib import pyplot as plt
import time
import pylab as py
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# -------------------------------------------
# Quantum walk in line with different shift
# -------------------------------------------


# 初始化量子态，是一个2*1维矩阵
def initQuanStat(X0, X1):
    initQuanStat = zeros([2, 1], complex)
    initQuanStat[0][0] = X0
    initQuanStat[1][0] = X1
    return initQuanStat


# 定义1D hadamard coin
def hadamardCoin():
    hadamardCoin = array([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]], complex)
    return hadamardCoin


# 定义1D phase coin
def phaseCoin(Psi):
    phaseCoin = array([[1, 0], [0, exp(1j * Psi)]], complex)
    return phaseCoin

# 根据shift的最大值和走了的步数定义空位置矩阵
def initPositionMap(steps, shiftNum, shiftGateNum):
    stepNum = 0
    for j in range(0, shiftGateNum):
        stepNum += power(2, j)
    dimension = stepNum * (steps - 1) + 1
    for i in range(0, shiftNum):
        dimension += power(2, i)
    positionMap = zeros([dimension, 2, 1], complex)
    return positionMap


# 对量子态经行coin变换
def coinOperator(coin, positionMap):
    dimension = shape(positionMap)[0]
    for i in range(dimension):
        positionMap[i] = dot(coin, positionMap[i])
    return positionMap


# 根据量子态进行位置变换，相当于一次walk
def shiftOperator(positionMap, step, shiftGateNum):
    for shiftNum in range(1, shiftGateNum + 1):
        newPositionMap = initPositionMap(step, shiftNum, shiftGateNum)
        coin = hadamardCoin()
        coinMap = coinOperator(coin, positionMap)
        for i in range(shape(coinMap)[0]):
            newPositionMap[i][0][0] += coinMap[i][0][0]
            newPositionMap[i + power(2, shiftNum - 1)][1][0] += coinMap[i][1][0]
        positionMap = newPositionMap
    return newPositionMap


# quantum walk 的整体封装，返回位置分布的量子态
def quantumWalk(X0, X1, steps, shiftGateNum):
    initPositionMap = zeros([1, 2, 1], complex)
    initPositionMap[0] = initQuanStat(X0, X1)
    for step in range(1, steps + 1):
        positionMap = initPositionMap
        initPositionMap = shiftOperator(positionMap, step, shiftGateNum)
    return initPositionMap


# 计算QW的位置分布
def QWDistribution(X0, X1, steps, shiftGateNum):
    positionMap = quantumWalk(X0, X1, steps, shiftGateNum)
    dimension = shape(positionMap)[0]
    distribution = zeros([dimension], dtype=float)
    sum = 0.0
    for i in range(dimension):
        distribution[i] = float(positionMap[i][0][0].real ** 2 + positionMap[i][0][0].imag ** 2 + \
                                positionMap[i][1][0].real ** 2 + positionMap[i][1][0].imag ** 2)
        sum += distribution[i]
    print('sum: %s') % sum
    return distribution


# 将结果写到文本文档
def writeQWtoArray(distribution):
    Filename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S') + '.txt'
    distrFlie = open(Filename, 'w+')
    for x in range(shape(distribution)[0]):
        distrFlie.write(str(distribution[x]) + '\n')
    distrFlie.close()


# 画出位置概率分布图
def PlotX(distribution, step, figName):
    plt.plot(distribution)
    plt.title('The Distribution of %s Quantum Walk with Different Shift') % step
    plt.xlabel('Started from the 0')
    plt.ylabel('Probability')
    # plt.show()
    plt.savefig('Fig/' + str(figName) + str(step) + '.png')
    plt.close()


# 画出QDS与QW的概率分布对比图
def PlotComp(distributionQDS, distributionQW, step, figName):
    QDS, = plt.plot(distributionQDS, 'r')
    QW, = plt.plot(distributionQW, 'b')
    plt.axis([0, 7 * step, 0, 0.27])
    plt.legend([QDS, QW, ], ['QDS', 'QW'])
    plt.title('The Compare between QDS and QW')
    plt.xlabel('X Position (started from the center)')
    plt.ylabel('Probability')
    # plt.show()
    plt.savefig('Fig/' + str(figName) + str(step) + '.png')
    plt.close()


# -------------------------------------------
# Quantum walk in cicle with different shift
# -------------------------------------------
def initQuanStatAverPosiCicle(X0, X1, Node):
    initQuanStat = zeros([Node, 2, 1], complex)
    for node in range(Node):
        initQuanStat[node][0][0] = X0 * 1 / sqrt(Node)
        initQuanStat[node][1][0] = X1 * 1 / sqrt(Node)
    return initQuanStat

def positionCicleMap(node):
    positionCicleMap = zeros([node, 2, 1], complex)
    return positionCicleMap


# 根据量子态进行位置变换，相当于一次walk
def shiftCicleOperator(positionMap, step, shiftGateNum, node):
    for shiftNum in range(1, shiftGateNum + 1):
        newPositionMap = positionCicleMap(node)
        coin = hadamardCoin()
        coinMap = coinOperator(coin, positionMap)
        for i in range(node):
            newPositionMap[i][0][0] += coinMap[i][0][0]
            if (i + power(2, shiftNum - 1) >= node):
                newPositionMap[i + power(2, shiftNum - 1) - node][1][0] += coinMap[i][1][0]
                # print('loop')
            else:
                newPositionMap[i + power(2, shiftNum - 1)][1][0] += coinMap[i][1][0]
        positionMap = newPositionMap
    return newPositionMap


# 加入phase coin 版本, 修正移位操作，实现complete graph
def shiftCicleWithPhaseOperator(positionMap, step, shiftGateNum, node, Psi, phaseGate):
    # 先整体走一步
    moveOne = positionMap.copy()
    for i in range(1, node):
        positionMap[i] = moveOne[i - 1]
    positionMap[0] = moveOne[node - 1]

    # 根据延时门再各自走对应步数
    for shiftNum in range(1, shiftGateNum + 1):
        newPositionMap = positionCicleMap(node)
        HadamardCoin = hadamardCoin()
        PhaseCoin = phaseCoin(Psi)
        coinMap = coinOperator(HadamardCoin, positionMap)
        if shiftNum == phaseGate:
            newMap = coinMap.copy()
            coinMap = coinOperator(PhaseCoin, newMap)
            print 'gate:%s phase coin' % shiftNum
        for i in range(node):
            newPositionMap[i][0][0] += coinMap[i][0][0]
            if (i + power(2, shiftNum - 1) >= node):
                newPositionMap[i + power(2, shiftNum - 1) - node][1][0] += coinMap[i][1][0]
                # print('loop')
            else:
                newPositionMap[i + power(2, shiftNum - 1)][1][0] += coinMap[i][1][0]
        positionMap = newPositionMap
    return newPositionMap


# phase coin ，complete graph with loop
def shiftCicleWithPhaseLoopOperator(positionMap, step, shiftGateNum, node, Psi, phaseGate):
    # 根据延时门各自走对应步数
    for shiftNum in range(1, shiftGateNum + 1):
        newPositionMap = positionCicleMap(node)
        HadamardCoin = hadamardCoin()
        PhaseCoin = phaseCoin(Psi)
        coinMap = coinOperator(HadamardCoin, positionMap)
        if shiftNum == phaseGate:
            newMap = coinMap.copy()
            coinMap = coinOperator(PhaseCoin, newMap)
            print 'gate:%s phase coin' % shiftNum
        for i in range(node):
            newPositionMap[i][0][0] += coinMap[i][0][0]
            if (i + power(2, shiftNum - 1) >= node):
                newPositionMap[i + power(2, shiftNum - 1) - node][1][0] += coinMap[i][1][0]
                # print('loop')
            else:
                newPositionMap[i + power(2, shiftNum - 1)][1][0] += coinMap[i][1][0]
        positionMap = newPositionMap
    return newPositionMap


# search position with marked coin ，complete graph with loop for 2 gate,4 node
def shiftCicleWithPhaseLoopSearchOperator(positionMap, step, shiftGateNum, node, Psi, phaseGate):
    # 根据延时门各自走对应步数
    for shiftNum in range(1, shiftGateNum + 1):
        newPositionMap = positionCicleMap(node)
        HadamardCoin = hadamardCoin()
        # PhaseCoin = phaseCoin(Psi)
        coinMap = coinOperator(HadamardCoin, positionMap)
        if shiftNum == phaseGate:
            # print 'gate:%s phase coin' % shiftNum
            newPositionMap[0][0][0] += coinMap[0][0][0]
            newPositionMap[4][1][0] += coinMap[0][1][0] * exp(1j * Psi)
            newPositionMap[4][0][0] += coinMap[4][0][0]
            newPositionMap[0][1][0] += coinMap[4][1][0] * exp(1j * Psi)
            for i in range(1, node):
                if i == 4:
                    print i
                else:
                    newPositionMap[i][0][0] += coinMap[i][0][0]
                    if (i + power(2, shiftNum - 1) >= node):
                        newPositionMap[i + power(2, shiftNum - 1) - node][1][0] += coinMap[i][1][0]
                        # print('loop')
                    else:
                        newPositionMap[i + power(2, shiftNum - 1)][1][0] += coinMap[i][1][0]
        else:
            for i in range(node):
                newPositionMap[i][0][0] += coinMap[i][0][0]
                if (i + power(2, shiftNum - 1) >= node):
                    newPositionMap[i + power(2, shiftNum - 1) - node][1][0] += coinMap[i][1][0]
                # print('loop')
                else:
                    newPositionMap[i + power(2, shiftNum - 1)][1][0] += coinMap[i][1][0]
        positionMap = newPositionMap
    return newPositionMap


# search position with marked point 0，实现complete graph
def shiftCicleWithPhaseSearchOperator(positionMap, step, shiftGateNum, node, Psi, phaseGate):
    # 先整体走一步
    moveOne = positionMap.copy()
    for i in range(1, node):
        positionMap[i] = moveOne[i - 1]
    positionMap[0] = moveOne[node - 1]

    # 根据延时门再各自走对应步数
    for shiftNum in range(1, shiftGateNum + 1):
        newPositionMap = positionCicleMap(node)
        HadamardCoin = hadamardCoin()
        # PhaseCoin = phaseCoin(Psi)
        coinMap = coinOperator(HadamardCoin, positionMap)
        for i in range(node):
            newPositionMap[i][0][0] += coinMap[i][0][0]
            if (i + power(2, shiftNum - 1) >= node):
                newPositionMap[i + power(2, shiftNum - 1) - node][1][0] += coinMap[i][1][0]
                # print('loop')
            else:
                newPositionMap[i + power(2, shiftNum - 1)][1][0] += coinMap[i][1][0]
        positionMap = newPositionMap
    # 标记点0，附加一个Psi的相位
    newPositionMap[0] = newPositionMap[0] * exp(1j * Psi)
    return newPositionMap


# quantum walk 的整体封装，返回位置分布的量子态
def quantumWalkCicle(X0, X1, steps, shiftGateNum, node):
    print 'begin'
    initPositionMap = zeros([node, 2, 1], complex)
    initPositionMap[0] = initQuanStat(X0, X1)
    for step in range(1, steps + 1):
        positionMap = initPositionMap
        initPositionMap = shiftCicleOperator(positionMap, step, shiftGateNum, node)
    return initPositionMap


'''
Release 1, for animate plotting
'''
# 计算概率分布
def QWCicleDistribution(X0, X1, steps, shiftGateNum, node):
    positionMap = quantumWalkCicle(X0, X1, steps, shiftGateNum, node)
    dimension = shape(positionMap)[0]
    distribution = zeros([dimension], dtype=float)
    sum = 0.0
    for i in range(dimension):
        distribution[i] = float(positionMap[i][0][0].real ** 2 + positionMap[i][0][0].imag ** 2 + \
                                positionMap[i][1][0].real ** 2 + positionMap[i][1][0].imag ** 2)
        sum += distribution[i]
    print('sum: %s') % sum
    return distribution


'''
Release 2 : for write data to txt file
'''
# quantum walk in cycle graph release for write data to txt file(直接将每一步的态与分布写到文件保存)
def QWCicleDistrWrite(X0, X1, steps, shiftGateNum, node):
    print 'begin'
    initPositionMap = zeros([node, 2, 1], complex)
    initPositionMap[0] = initQuanStat(X0, X1)
    DsitriFilename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S_') + 'Position' + str(shiftGateNum) + \
                     str(node) + str(steps) + '.txt'
    StateFilename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S_') + 'State' + str(shiftGateNum) + \
                    str(node) + str(steps) + '.txt'
    distrFile = open(DsitriFilename, 'w+')
    stateFile = open(StateFilename, 'w+')
    for step in range(1, steps + 1):
        print 'step: %s' % step
        positionMap = initPositionMap
        initPositionMap = shiftCicleOperator(positionMap, step, shiftGateNum, node)
        dimension = shape(initPositionMap)[0]
        distribution = zeros([dimension], dtype=float)
        sum = 0.0
        for i in range(dimension):
            distribution[i] = float(initPositionMap[i][0][0].real ** 2 + initPositionMap[i][0][0].imag ** 2 + \
                                    initPositionMap[i][1][0].real ** 2 + initPositionMap[i][1][0].imag ** 2)
            sum += distribution[i]
            stateFile.write(str(initPositionMap[i][0][0]) + str(initPositionMap[i][1][0]) + '\t')
            distrFile.write(str(distribution[i]) + '\t')
        print('sum: %s') % sum
        distrFile.write('\n')
        stateFile.write('\n')
    stateFile.close()
    distrFile.close()
    print 'finish'


'''
Release 3 : add phase coin and modified for complete graph
'''
# quantum walk in cycle graph release for phase coin (添加phase coin，对shift operator进行了修正)
def QWCicleWithPhaseDistrWrite(X0, X1, steps, shiftGateNum, node, Psi, gate):
    print 'begin'
    initPositionMap = zeros([node, 2, 1], complex)
    initPositionMap[0] = initQuanStat(X0, X1)
    # initPositionMap = initQuanStatAverPosiCicle(X0, X1,node)
    PositionPsiFilename = 'Data/K5_X0' + str(X0) + '_X1' + str(X1) + '_' + str(shiftGateNum) + '-' + str(
        node) + '_Steps' + str(steps) + '.txt'
    PosiFile = open(PositionPsiFilename, 'a')
    # DsitriFilename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S') + '_Position_' + str(shiftGateNum) + \
    #                  str(node) + str(steps) + '.txt'
    # StateFilename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S') + '_State_' + str(shiftGateNum) + \
    #                 str(node) + str(steps) + '.txt'
    # distrFile = open(DsitriFilename, 'w+')
    # stateFile = open(StateFilename, 'w+')
    # infoS = 'State: X0 %s X1 %s, steps: %s, shiftGateNum: %s, node: %s, Psi: %s, gate: %s\n' % (
    # X0, X1, steps, shiftGateNum, node, Psi, gate)
    # infoD = 'State: X0 %s X1 %s, steps: %s, shiftGateNum: %s, node: %s, Psi: %s, gate: %s \n' % (
    # X0, X1, steps, shiftGateNum, node, Psi, gate)
    # stateFile.write(infoS)
    # distrFile.write(infoD)
    for step in range(1, steps + 1):
        print 'step: %s' % step
        positionMap = initPositionMap
        initPositionMap = shiftCicleWithPhaseOperator(positionMap, step, shiftGateNum, node, Psi, gate)
        dimension = shape(initPositionMap)[0]
        distribution = zeros([dimension], dtype=float)
        sum = 0.0
        PosiFile.write(str(Psi) + '\t')
        PosiFile.write(str(step) + '\t')
        for i in range(dimension):
            distribution[i] = float(initPositionMap[i][0][0].real ** 2 + initPositionMap[i][0][0].imag ** 2 + \
                                    initPositionMap[i][1][0].real ** 2 + initPositionMap[i][1][0].imag ** 2)
            sum += distribution[i]
            PosiFile.write(str(distribution[i]) + '\t')
            # stateFile.write(str(initPositionMap[i][0][0]) + str(initPositionMap[i][1][0]) + '\t')
            # distrFile.write(str(distribution[i]) + '\t')
        PosiFile.write('\n')
        print('sum: %s') % sum
    # distrFile.write('\n')
    #     stateFile.write('\n')
    # stateFile.close()
    # distrFile.close()
    PosiFile.close()
    print 'finish'


'''
Release 4 : add phase coin and modified for complete graph with loop
'''


# quantum walk in cycle graph with loop release for phase coin
def QWCicleWithPhaseLoopDistrWrite(X0, X1, steps, shiftGateNum, node, Psi, gate):
    print 'begin'
    initPositionMap = zeros([node, 2, 1], complex)
    initPositionMap[0] = initQuanStat(X0, X1)
    #initPositionMap=initQuanStatAverPosiCicle(X0,X1,node)
    DsitriFilename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S') + '_Position_' + str(shiftGateNum) + \
                     str(node) + str(steps) + '.txt'
    StateFilename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S') + '_State_' + str(shiftGateNum) + \
                    str(node) + str(steps) + '.txt'
    distrFile = open(DsitriFilename, 'w+')
    stateFile = open(StateFilename, 'w+')
    infoS = 'State: X0 %s X1 %s, steps: %s, shiftGateNum: %s, node: %s, Psi: %s, gate: %s\n' % (
    X0, X1, steps, shiftGateNum, node, Psi, gate)
    infoD = 'State: X0 %s X1 %s, steps: %s, shiftGateNum: %s, node: %s, Psi: %s, gate: %s \n' % (
    X0, X1, steps, shiftGateNum, node, Psi, gate)
    stateFile.write(infoS)
    distrFile.write(infoD)
    for step in range(1, steps + 1):
        print 'step: %s' % step
        positionMap = initPositionMap
        initPositionMap = shiftCicleWithPhaseLoopOperator(positionMap, step, shiftGateNum, node, Psi, gate)
        dimension = shape(initPositionMap)[0]
        distribution = zeros([dimension], dtype=float)
        sum = 0.0
        for i in range(dimension):
            distribution[i] = float(initPositionMap[i][0][0].real ** 2 + initPositionMap[i][0][0].imag ** 2 + \
                                    initPositionMap[i][1][0].real ** 2 + initPositionMap[i][1][0].imag ** 2)
            sum += distribution[i]
            stateFile.write(str(initPositionMap[i][0][0]) + str(initPositionMap[i][1][0]) + '\t')
            distrFile.write(str(distribution[i]) + '\t')
        print('sum: %s') % sum
        distrFile.write('\n')
        stateFile.write('\n')
    stateFile.close()
    distrFile.close()
    print 'finish'


'''
Release 5 : add phase coin and modified for complete graph with loop, write position
            probability file with Psi
'''


# quantum walk in cycle graph with loop release for phase coin
def QWCicleWithPhaseLoopDistrWritePosi(X0, X1, steps, shiftGateNum, node, Psi, gate):
    print 'begin'
    initPositionMap = zeros([node, 2, 1], complex)
    # initPositionMap[0] = initQuanStat(X0, X1)
    initPositionMap = initQuanStatAverPosiCicle(X0, X1, node)
    PositionPsiFilename = 'Data/Loop_X0' + str(X0) + '_X1' + str(X1) + '_' + str(shiftGateNum) + '-' + str(
        node) + '_Steps' + str(steps) + 'Aver.txt'
    PosiFile = open(PositionPsiFilename, 'a')
    for step in range(1, steps + 1):
        print 'step: %s' % step
        positionMap = initPositionMap
        initPositionMap = shiftCicleWithPhaseLoopOperator(positionMap, step, shiftGateNum, node, Psi, gate)
        dimension = shape(initPositionMap)[0]
        distribution = zeros([dimension], dtype=float)
        sum = 0.0
        for i in range(dimension):
            distribution[i] = float(initPositionMap[i][0][0].real ** 2 + initPositionMap[i][0][0].imag ** 2 + \
                                    initPositionMap[i][1][0].real ** 2 + initPositionMap[i][1][0].imag ** 2)
            sum += distribution[i]
            if i == 0:
                PosiFile.write(str(Psi) + '\t')
                PosiFile.write(str(step) + '\t')
                PosiFile.write(str(distribution[i]) + '\n')
        print('sum: %s') % sum
    PosiFile.close()
    print 'finish'


'''
Release 6 : Search one position by marked in complete graph with loop
'''


# quantum walk search in cycle graph with loop
def QWCicleWithPhaseLoopSearch(X0, X1, steps, shiftGateNum, node, Psi, gate):
    print 'begin'
    initPositionMap = zeros([node, 2, 1], complex)
    initPositionMap[0] = initQuanStat(X0, X1)
    # initPositionMap=initQuanStatAverPosiCicle(X0,X1,node)
    # DsitriFilename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S') + '_Search_Position_' + str(shiftGateNum) + \
    #                  str(node) + str(steps) + '.txt'
    # StateFilename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S') + '_Search_State_' + str(shiftGateNum) + \
    #                 str(node) + str(steps) + '.txt'
    # distrFile = open(DsitriFilename, 'w+')
    # stateFile = open(StateFilename, 'w+')
    # infoS = 'Search State: X0 %s X1 %s, steps: %s, shiftGateNum: %s, node: %s, Psi: %s, gate: %s\n' % (
    # X0, X1, steps, shiftGateNum, node, Psi, gate)
    # infoD = 'Search State: X0 %s X1 %s, steps: %s, shiftGateNum: %s, node: %s, Psi: %s, gate: %s \n' % (
    # X0, X1, steps, shiftGateNum, node, Psi, gate)
    # stateFile.write(infoS)
    # distrFile.write(infoD)
    PositionPsiFilename = 'Data/Loop_Search_X0' + str(X0) + '_X1' + str(X1) + '_' + str(shiftGateNum) + '-' + str(
        node) + '_Steps' + str(steps) + '.txt'
    PosiFile = open(PositionPsiFilename, 'a')
    for step in range(1, steps + 1):
        print 'step: %s' % step
        positionMap = initPositionMap
        initPositionMap = shiftCicleWithPhaseLoopSearchOperator(positionMap, step, shiftGateNum, node, Psi, gate)
        dimension = shape(initPositionMap)[0]
        distribution = zeros([dimension], dtype=float)
        sum = 0.0
        for i in range(dimension):
            distribution[i] = float(initPositionMap[i][0][0].real ** 2 + initPositionMap[i][0][0].imag ** 2 + \
                                    initPositionMap[i][1][0].real ** 2 + initPositionMap[i][1][0].imag ** 2)
            sum += distribution[i]
            if i == 1:
                PosiFile.write(str(Psi) + '\t')
                PosiFile.write(str(step) + '\t')
                PosiFile.write(str(distribution[i]) + '\n')
                # stateFile.write(str(initPositionMap[i][0][0]) + str(initPositionMap[i][1][0]) + '\t')
                # distrFile.write(str(distribution[i]) + '\t')
        print('sum: %s') % sum
    # distrFile.write('\n')
    #     stateFile.write('\n')
    # stateFile.close()
    # distrFile.close()
    PosiFile.close()
    print 'finish'


'''
Release 7 : Search one position by marked in complete graph
'''


# quantum walk in cycle graph release for phase coin (添加phase coin，对shift operator进行了修正)
def QWCicleWithPhaseSearch(X0, X1, steps, shiftGateNum, node, Psi, gate):
    print 'begin'
    initPositionMap = zeros([node, 2, 1], complex)
    # initPositionMap[0] = initQuanStat(X0, X1)
    initPositionMap = initQuanStatAverPosiCicle(X0, X1, node)
    PositionPsiFilename = 'Data/Search mark_0 X0' + str(X0) + '_X1' + str(X1) + '_' + str(shiftGateNum) + '-' + str(
        node) + '_Steps' + str(steps) + 'Aver.txt'
    PosiFile = open(PositionPsiFilename, 'a')
    for step in range(1, steps + 1):
        print 'step: %s' % step
        positionMap = initPositionMap
        initPositionMap = shiftCicleWithPhaseSearchOperator(positionMap, step, shiftGateNum, node, Psi, gate)
        dimension = shape(initPositionMap)[0]
        distribution = zeros([dimension], dtype=float)
        sum = 0.0
        PosiFile.write(str(Psi) + '\t')
        PosiFile.write(str(step) + '\t')
        for i in range(dimension):
            distribution[i] = float(initPositionMap[i][0][0].real ** 2 + initPositionMap[i][0][0].imag ** 2 + \
                                    initPositionMap[i][1][0].real ** 2 + initPositionMap[i][1][0].imag ** 2)
            sum += distribution[i]
            PosiFile.write(str(distribution[i]) + '\t')
        print('sum: %s') % sum
        PosiFile.write('\n')
    PosiFile.close()
    print 'finish'

# 对位置列表进行位移，使原点保持不变
#TODO 位置变换有点问题，暂时不用
def ciclePosiTrans(positionMap, steps, shiftGateNum):
    node = shape(positionMap)[0]
    positionMapTrans = zeros([node], float)
    initNode = (power(2, shiftGateNum) - 1) * steps % node
    for i in range(node):
        positionMapTrans[i] = positionMap[(initNode + i) % node]
    return positionMapTrans


# 画出2D位置分布图
def PlotCicle(distribution, steps, shiftGateNum, figName):
    node = shape(distribution)[0]
    radius = 1
    x = zeros([node], float)
    y = zeros([node], float)
    for i in range(node):
        x[i] = sin(i * 2 * math.pi / node) * radius
        y[i] = cos(i * 2 * math.pi / node) * radius

    plt.figure(1, figsize=(20, 9))
    ax1 = plt.subplot(121)
    plt.sca(ax1)
    plt.title('Distribution of %s steps Quantum Walk in Cicle' % steps)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    #   plt.imshow(positionMap)
    #    plt.axis([0, 2 * int(radius) + 3, 0, 2 * int(radius) + 3])
    #    plt.grid(True)
    plt.scatter(x, y, distribution * 2000, c='r', marker='o')
    plt.axis([-1.5, 1.5, -1.5, 1.5])
    plt.subplot(122)
    plt.plot(distribution)
    plt.axis([0, node - 1, 0, 1])
    plt.title('Distribution of %s steps QW with Different Shift' % steps)
    plt.xlabel('Started from 0')
    plt.ylabel('Probability')
    # plt.show()
    plt.savefig('Fig/' + str(figName) + str(steps) + '_' + str(shiftGateNum) + '.png')
    plt.close()
