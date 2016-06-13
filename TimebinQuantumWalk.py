#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'levitan'

from numpy import *
from matplotlib import pyplot as plt
import time
import pylab as py
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation


# ----------------------------------------------
# Quantum walk in Time-bin architecture design
# ----------------------------------------------

def initQuanStatList(X0, X1, count):
    initQuanStat = zeros([count, 2, 1], complex)
    for node in range(0, count):
        initQuanStat[node][0][0] = X0 * 1 / sqrt(count)
        initQuanStat[node][1][0] = X1 * 1 / sqrt(count)
    return initQuanStat


# 定义1D hadamard coin
def hadamardCoin():
    hadamardCoin = array([[1 / sqrt(2), 1 / sqrt(2)], [1 / sqrt(2), -1 / sqrt(2)]], complex)
    return hadamardCoin


# 对量子态经行coin变换
def coinOperator(coin, positionMap):
    dimension = shape(positionMap)[0]
    for i in range(dimension):
        positionMap[i] = dot(coin, positionMap[i])
    return positionMap


def positionList(steps, node, delayT):
    PositionList = zeros([steps * (delayT + node), 2, 1], complex)
    return PositionList


# search position with marked line
def shiftWithPhaseSearchOperator(positionMap, step, shiftGateNum, node, delayT, Psi):
    # 根据延时门再各自走对应步数
    count = shape(positionMap)[0]
    movePositionMap = positionList(step, node, delayT)
    for point in range(count):
        movePositionMap[point + node + 1] = positionMap[point]
    positionMap = movePositionMap
    for shiftNum in range(1, shiftGateNum + 1):
        newPositionMap = positionList(step, node)
        HadamardCoin = hadamardCoin()
        # PhaseCoin = phaseCoin(Psi)
        coinMap = coinOperator(HadamardCoin, positionMap)
        for i in range((step - 1) * delayT, (step - 1) * delayT + node):
            newPositionMap[i][0][0] += coinMap[i][0][0]
            newPositionMap[i + power(2, shiftGateNum - 1)][1][0] += coinMap[i][1][0]
        positionMap = newPositionMap
    # 标记点0，附加一个Psi的相位
    newPositionMap[step * (node + 1)][0][0] = newPositionMap[step * (node + 1)][0][0] * exp(1j * Psi)
    newPositionMap[step * (node + 1)][1][0] = newPositionMap[step * (node + 1)][1][0] * exp(1j * Psi)
    # if step%2==1:
    #     newPositionMap[0] = newPositionMap[0] * exp(1j * Psi)
    #     print step
    return newPositionMap


# quantum walk in cycle graph release for phase coin (添加phase coin，对shift operator进行了修正)
def TimebinQW(X0, X1, count, steps, shiftGateNum, node, Phase):
    print 'begin'
    # initPositionMap = zeros([node, 2, 1], complex)
    # initPositionMap[0] = initQuanStat(X0, X1)
    initPositionMap = initQuanStatList(X0, X1, count)
    # print initPositionMap
    StateFilename = 'Data/Timebin-' + time.strftime('%Y%m%d-%H-%M-%S') + '_State_' + str(shiftGateNum) + \
                    str(node) + str(steps) + '.txt'
    stateFile = open(StateFilename, 'w+')
    infoS = 'Search State: X0 %s X1 %s, steps: %s, shiftGateNum: %s, node: %s, Phase: %s\n' % (
        X0, X1, steps, shiftGateNum, node, Phase)
    stateFile.write(infoS)
    PositionPsiFilename = 'Data/Timebin-position X0' + str(X0) + '_X1' + str(X1) + '_' + str(shiftGateNum) + '-' + str(
            node) + '_Steps' + str(steps) + time.strftime(' %Y%m%d-%H-%M-%S') + 'Aver.txt'
    PosiFile = open(PositionPsiFilename, 'a')
    for step in range(1, steps + 1):
        print 'step: %s' % step
        positionMap = initPositionMap
        initPositionMap = shiftWithPhaseSearchOperator(positionMap, step, shiftGateNum, node, Phase)
        # print initPositionMap
        dimension = shape(initPositionMap)[0]
        distribution = zeros([dimension], dtype=float)
        sum = 0.0
        PosiFile.write(str(Phase) + '\t')
        PosiFile.write(str(step) + '\t')
        for i in range(dimension):
            distribution[i] = float(initPositionMap[i][0][0].real ** 2 + initPositionMap[i][0][0].imag ** 2 + \
                                    initPositionMap[i][1][0].real ** 2 + initPositionMap[i][1][0].imag ** 2)
            sum += distribution[i]
            PosiFile.write(str(distribution[i]) + '\t')
            stateFile.write(str(initPositionMap[i][0][0].real) + ' ' + str(initPositionMap[i][1][0].real) + '\t')
        print('sum: %s') % sum
        PosiFile.write('\n')
        stateFile.write('\n')
    stateFile.close()
    PosiFile.close()
    print 'finish'
