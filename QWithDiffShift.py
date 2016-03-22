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
import pylab as py
from mpl_toolkits.mplot3d import Axes3D


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


# 根据shift的最大值和走了的步数定义空位置矩阵
def initPositionMap(steps, shiftNum, shiftGateNum):
    stepNum = 0
    for j in range(0, shiftGateNum):
        stepNum += power(2, j)
    dimension = 2 * stepNum * (steps - 1) + 1
    for i in range(1, shiftNum + 1):
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
            newPositionMap[i + power(2, shiftNum)][1][0] += coinMap[i][1][0]
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
def writeQWtoArray(distribution, filename):
    Filename = 'Data/' + filename
    distrFlie = open(Filename, 'w+')
    for x in range(shape(distribution)[0]):
        distrFlie.write(str(distribution[x]) + '\n')
    distrFlie.close()


# 画出位置概率分布图
def PlotX(distribution, step):
    plt.plot(distribution)
    plt.title('The Distribution of Quantum Walk with Different Shift')
    plt.xlabel('Started from the center')
    plt.ylabel('Probability')
    # plt.show()
    plt.savefig('Fig/QDS_Cicle' + str(step) + '.png')
    plt.close()


# 画出QDS与QW的概率分布对比图
def PlotComp(distributionQDS, distributionQW, step):
    QDS, = plt.plot(distributionQDS, 'r')
    QW, = plt.plot(distributionQW, 'b')
    plt.axis([0, 14 * step, 0, 0.27])
    plt.legend([QDS, QW, ], ['QDS', 'QW'])
    plt.title('The Compare between QDS and QW')
    plt.xlabel('X Position (started from the center)')
    plt.ylabel('Probability')
    # plt.show()
    plt.savefig('Fig/QDS-VS-QW_' + str(step) + '.png')
    plt.close()


# -------------------------------------------
# Quantum walk in cicle with different shift
# -------------------------------------------

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
            if (i + power(2, shiftNum) >= node):
                newPositionMap[i + power(2, shiftNum) - node][1][0] += coinMap[i][1][0]
                print('loop')
            else:
                newPositionMap[i + power(2, shiftNum)][1][0] += coinMap[i][1][0]
        positionMap = newPositionMap
    return newPositionMap


# quantum walk 的整体封装，返回位置分布的量子态
def quantumWalkCicle(X0, X1, steps, shiftGateNum, node):
    initPositionMap = zeros([node, 2, 1], complex)
    initPositionMap[0] = initQuanStat(X0, X1)
    for step in range(1, steps + 1):
        positionMap = initPositionMap
        initPositionMap = shiftCicleOperator(positionMap, step, shiftGateNum, node)
    return initPositionMap


# 计算概率分布
def QWDistribution(X0, X1, steps, shiftGateNum, node):
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


# 画出2D位置分布图
def PlotCicle(distribution, steps):
    node = shape(distribution)[0]
    radius = node / (2 * math.pi)
    positionMap = zeros([2 * int(radius) + 4, 2 * int(radius) + 4])
    for i in range(node):
        x = int(sin(i * 2 * math.pi / node) * radius) + int(radius) + 2
        y = int(cos(i * 2 * math.pi / node) * radius) + int(radius) + 2
        positionMap[x][y] = distribution[i]
    plt.figure(1)
    ax1 = plt.subplot(111)
    plt.sca(ax1)
    plt.title('2D distribution of %s steps Quantum Walk in Cicle' % steps)
    plt.xlabel('X Position')
    plt.ylabel('Y Position')
    plt.imshow(positionMap)
    plt.axis([0, 2 * int(radius) + 4, 0, 2 * int(radius) + 4])
    plt.grid(True)
    plt.savefig('Fig/QDSC_' + str(steps) + '.png')
    plt.close()

    # fig = py.figure()
    # ax = Axes3D(fig)
    # X = arange(0, 2*int(radius)+4, 1)
    # Y = arange(0, 2*int(radius)+4, 1)
    # X, Y = meshgrid(X, Y)
    # Z = positionMap[X][Y]
    #
    # ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
    #
    # py.show()
