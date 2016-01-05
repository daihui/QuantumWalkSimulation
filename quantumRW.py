#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'levitan'

import math
from numpy import *
import numpy as np
import random
from matplotlib import pyplot as plt
import copy

dimension = 1


def initQuantumStateList(X0, X1, Y0, Y1, totalSteps):
    initquantumStateList = zeros([2 * totalSteps + 1, 2 * totalSteps + 1, 2, 2], dtype=complex)
    initquantumStateList[totalSteps][totalSteps][0][0] = complex(X0)
    initquantumStateList[totalSteps][totalSteps][0][1] = complex(X1)
    initquantumStateList[totalSteps][totalSteps][1][0] = complex(Y0)
    initquantumStateList[totalSteps][totalSteps][1][1] = complex(Y1)
    return initquantumStateList


# print  quantumState(1,1,0,0,1,1,0,0)

def hadamardCoin(quantumStateList, totalSteps):
    global dimension
    for x in range(dimension):
        for y in range(dimension):
            tempState = zeros([2, 2], dtype=complex)
            tempState = copy.deepcopy(
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y])
            quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][0][
                0] = complex((tempState[0][0] + tempState[0][1]) / sqrt(2))
            quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][0][
                1] = complex((tempState[0][0] - tempState[0][1]) / sqrt(2))
            quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][1][
                0] = complex((tempState[1][0] + tempState[1][1]) / sqrt(2))
            quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][1][
                1] = complex((tempState[1][0] - tempState[1][1]) / sqrt(2))
    # print quantumStateList
    return quantumStateList


# qs=quantumState(0,1,0,0,0,1,0,0)
# print qs
# print  hadamardCoin(qs)

def shiftOperator(quantumStateList, totalSteps):
    global dimension
    newQuanStatList = zeros([2 * totalSteps + 1, 2 * totalSteps + 1, 2, 2], dtype=complex)
    for x in range(dimension):
        for y in range(dimension):
            newQuanStat1 = zeros([2, 2], dtype=complex)
            newQuanStat1[0][0] = \
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][0][0]
            newQuanStat1[0][1] = 0.0
            newQuanStat1[1][0] = \
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][1][0]
            newQuanStat1[1][1] = 0.0
            newQuanStatList[totalSteps - (dimension - 1) / 2 + x - 1][
                totalSteps - (dimension - 1) / 2 + y - 1] += (newQuanStat1 / sqrt(2))

            newQuanStat2 = zeros([2, 2], dtype=complex)
            newQuanStat2[0][0] = \
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][0][0]
            newQuanStat2[0][1] = 0.0
            newQuanStat2[1][0] = 0.0
            newQuanStat2[1][1] = \
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][1][1]
            newQuanStatList[totalSteps - (dimension - 1) / 2 + x - 1][
                totalSteps - (dimension - 1) / 2 + y + 1] += (newQuanStat2 / sqrt(2))

            newQuanStat3 = zeros([2, 2], dtype=complex)
            newQuanStat3[0][0] = 0.0
            newQuanStat3[0][1] = \
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][0][1]
            newQuanStat3[1][0] = 0.0
            newQuanStat3[1][1] = \
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][1][1]
            newQuanStatList[totalSteps - (dimension - 1) / 2 + x + 1][
                totalSteps - (dimension - 1) / 2 + y + 1] += (newQuanStat3 / sqrt(2))

            newQuanStat4 = zeros([2, 2], dtype=complex)
            newQuanStat4[0][0] = 0.0
            newQuanStat4[0][1] = \
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][0][1]
            newQuanStat4[1][0] = \
                quantumStateList[totalSteps - (dimension - 1) / 2 + x][totalSteps - (dimension - 1) / 2 + y][1][0]
            newQuanStat4[1][1] = 0.0
            newQuanStatList[totalSteps - (dimension - 1) / 2 + x + 1][
                totalSteps - (dimension - 1) / 2 + y - 1] += (newQuanStat4 / sqrt(2))
    dimension += 2
    return newQuanStatList

def quantumWalker(X0, X1, Y0, Y1, totalSteps,plotSteps):
    global dimension
    initStateList = initQuantumStateList(X0, X1, Y0, Y1, totalSteps)
    newQuanStatList = zeros([2 * totalSteps + 1, 2 * totalSteps + 1, 2, 2], dtype=complex)
    shiftQuanStatList = initStateList
    for i in range(1,totalSteps+1):
        newQuanStatList = hadamardCoin(shiftQuanStatList, totalSteps)
        shiftQuanStatList = shiftOperator(newQuanStatList, totalSteps)
        if (i!=0)&(i%plotSteps == 0) :
            print dimension
            print i
            plotQW=distriQW(shiftQuanStatList,dimension,totalSteps)
            Plot2D(plotQW,i)
    dimension = 1
    return shiftQuanStatList


def distriQW(quantumWalkerList, dim,totalSteps):
    distribution = zeros([2 * totalSteps + 1, 2 * totalSteps + 1], dtype=float)
    sum = 0.0
        # print quantumWalkerList
    for x in range(dim):
        for y in range(dim):
            distribution[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y] += float(
                    abs((quantumWalkerList[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y][0][0].real ** 2 + quantumWalkerList[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y][0][0].imag ** 2))
                    + abs((quantumWalkerList[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y][0][1].real ** 2 + quantumWalkerList[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y][0][1].imag ** 2))
                    + abs((quantumWalkerList[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y][1][0].real ** 2 + quantumWalkerList[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y][1][0].imag ** 2))
                    + abs((quantumWalkerList[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y][1][1].real ** 2 + quantumWalkerList[totalSteps-(dim-1)/2+x][totalSteps-(dim-1)/2 +y][1][1].imag ** 2)))
            sum += distribution[totalSteps-dim +x][totalSteps-dim +y]
    print('Sum= %s' % sum)
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


def Plot2D(qw,steps):
    plt.figure(1)
    ax1 = plt.subplot(111)
    plt.sca(ax1)
    plt.title('2D distribution of %s steps Quantum Walk with hadamard coin' %steps)
    plt.xlabel('X Position (started in center)')
    plt.ylabel('Y Position (started in center)')
    plt.imshow(qw)
    plt.savefig('QW_'+str(steps)+'.png')
    plt.close()


def PlotX(qw, Y):
    qwX = qw[:][Y]
    plt.plot(qwX)
    plt.title('a Slice of 2D distribution of Quantum Walk')
    plt.xlabel('Position(started in %s)' % Y)
    plt.ylabel('Probability')
    plt.show()
