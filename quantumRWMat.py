#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'levitan'

"""
This is matrix release for 2D quantum walk simulation.
量子游走的基本过程：有一个初始量子态，coin是一个幺正变换，一次游走即coin对量子态变换一次
然后根据量子态walk一步，得到一个位置概率分布，如此反复。
"""

from numpy import *
from matplotlib import pyplot as plt


# 初始化量子态，是一个对角矩阵
def initQuanStat(X0, X1, Y0, Y1):
    initQuanStat = zeros([4, 4], complex)
    initQuanStat[0][0] = X0
    initQuanStat[1][1] = X1
    initQuanStat[2][2] = Y0
    initQuanStat[3][3] = Y1
    return initQuanStat


# 定义2D hadamard coin，实际是2个1D Coin的直积态
def hadamardCoin():
    hadamardCoin = array(([1 / sqrt(2), 1 / sqrt(2), 0, 0], [1 / sqrt(2), -1 / sqrt(2), 0, 0]
                          , [0, 0, 1 / sqrt(2), 1 / sqrt(2)], [0, 0, 1 / sqrt(2), -1 / sqrt(2)]), complex)
    return hadamardCoin


# 根据走了的步数定义空位置矩阵
def initPositionMap(steps):
    positionMap = zeros([2 * steps + 1, 2 * steps + 1, 4, 4], complex)
    return positionMap


# 对量子态经行coin变换
def coinOperator(positionMap, coin):
    dimension = shape(positionMap)[0]
    for i in range(dimension):
        for j in range(dimension):
            positionMap[i][j] = dot(positionMap[i][j], coin)
    return positionMap


# 根据量子态进行位置变换，相当于一次walk
def shiftOperator(coinMap, step):
    newPositionMap = initPositionMap(step)
    for i in range(2 * step - 1):
        for j in range(2 * step - 1):
            newPositionMap[i][j][0][0] += coinMap[i][j][0][0]
            newPositionMap[i][j][1][0] += coinMap[i][j][1][0]
            newPositionMap[i][j][2][2] += coinMap[i][j][2][2]
            newPositionMap[i][j][3][2] += coinMap[i][j][3][2]

            newPositionMap[i][j + 2][0][1] += coinMap[i][j][0][1]
            newPositionMap[i][j + 2][1][1] += coinMap[i][j][1][1]
            newPositionMap[i][j + 2][2][2] += coinMap[i][j][2][2]
            newPositionMap[i][j + 2][3][2] += coinMap[i][j][3][2]

            newPositionMap[i + 2][j][0][0] += coinMap[i][j][0][0]
            newPositionMap[i + 2][j][1][0] += coinMap[i][j][1][0]
            newPositionMap[i + 2][j][2][3] += coinMap[i][j][2][3]
            newPositionMap[i + 2][j][3][3] += coinMap[i][j][3][3]

            newPositionMap[i + 2][j + 2][0][1] += coinMap[i][j][0][1]
            newPositionMap[i + 2][j + 2][1][1] += coinMap[i][j][1][1]
            newPositionMap[i + 2][j + 2][2][3] += coinMap[i][j][2][3]
            newPositionMap[i + 2][j + 2][3][3] += coinMap[i][j][3][3]

    return newPositionMap


# quantum walk 的整体封装，返回位置分布的量子态
def quantumWalk(X0, X1, Y0, Y1, steps):
    initPositionMap = zeros([1, 1, 4, 4], complex)
    initPositionMap[0][0] = initQuanStat(X0, X1, Y0, Y1)
    coin = hadamardCoin()
    for step in range(1, steps + 1):
        positionMap = initPositionMap
        coinMap = coinOperator(positionMap, coin)
        initPositionMap = shiftOperator(coinMap, step)
    return initPositionMap


# 计算QW的位置分布
def QWDistribution(X0, X1, Y0, Y1, steps):
    positionMap = quantumWalk(X0, X1, Y0, Y1, steps)
    dimension = shape(positionMap)[0]
    distribution = zeros([dimension, dimension], dtype=float)
    sum = 0.0
    for i in range(dimension):
        for j in range(dimension):
            distribution[i][j] = float((positionMap[i][j][0][0].real ** 2 + positionMap[i][j][0][0].imag ** 2 + \
                                        positionMap[i][j][1][0].real ** 2 + positionMap[i][j][1][0].imag ** 2 + \
                                        positionMap[i][j][0][1].real ** 2 + positionMap[i][j][0][1].imag ** 2 + \
                                        positionMap[i][j][1][1].real ** 2 + positionMap[i][j][1][1].imag ** 2 + \
                                        positionMap[i][j][2][2].real ** 2 + positionMap[i][j][2][2].imag ** 2 + \
                                        positionMap[i][j][3][2].real ** 2 + positionMap[i][j][3][2].imag ** 2 + \
                                        positionMap[i][j][2][3].real ** 2 + positionMap[i][j][2][3].imag ** 2 + \
                                        positionMap[i][j][3][3].real ** 2 + positionMap[i][j][3][3].imag ** 2))
            sum += distribution[i][j]
    return distribution / sum


def writeQWtoArray(distribution, filename):
    distrFlie = open(filename, 'w+')
    for x in range(shape(distribution)[0]):
        for y in range(shape(distribution)[1]):
            distrFlie.write(str(distribution[x][y]) + '\t')
        distrFlie.write('\n')
    distrFlie.close()


def writeQWtoList(distribution, filename):
    distrFlie = open(filename, 'w+')
    for x in range(shape(distribution)[0]):
        for y in range(shape(distribution)[1]):
            distrFlie.write(str(x) + '\t' + str(y) + '\t' + str(distribution[x][y]) + '\n')
    distrFlie.close()


def Plot2D(qw, steps):
    plt.figure(1)
    ax1 = plt.subplot(111)
    plt.sca(ax1)
    plt.title('2D distribution of %s steps Quantum Walk with hadamard coin' % steps)
    plt.xlabel('X Position (started in center)')
    plt.ylabel('Y Position (started in center)')
    plt.imshow(qw)
    plt.savefig('QWM_' + str(steps) + '.png')
    plt.close()


def PlotX(qw, Y):
    qwX = qw[:][Y]
    plt.plot(qwX)
    plt.title('a Slice of 2D distribution of Quantum Walk')
    plt.xlabel('Position(started in %s)' % Y)
    plt.ylabel('Probability')
    plt.show()
