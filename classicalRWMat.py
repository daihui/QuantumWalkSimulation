#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'levitan'

"""
This is a matrix release for 2D classic random walk simulation.
经典随机游走的基本过程：在一个初始位置，投一次coin（随机选择），根据coin的结果，
选择向某一个方向走一步，然后再投一次coin，周而复始。
classicalRanMun():产生一个随机coin
classcalWalkerPosition():walker的初始位置，设为(0,0)
classicalWalk():根据参数walkNum随机游走walkNum步，返回最后位置walkerPosition
classicalRWDistr():重复satNum次随机游走，得到walkerPosition的统计分布
Plot2D():画图函数，画出2D的经典随机游走位置概率分布
"""

from numpy import *
import random
from matplotlib import pyplot as plt

def classicalRanNum():
    return mat([[random.choice([1,-1])],[random.choice([1,-1])]],int)

def classicalWalkerPosition():
    return mat([[0],[0]],int)

def classicalWalk(walkNum):
    walkerPosition = classicalWalkerPosition()
    for i in range(0, walkNum):
        coin= classicalRanNum()
        walkerPosition+=coin
    return walkerPosition

def classicalRWDistr(walkNum, matrixNum,satNum):
    walkerCount = zeros([2 *matrixNum + 1, 2 * matrixNum + 1])
    for i in range(0, satNum):
        walker = classicalWalk(walkNum)
        walkerCount[int(walker[0])+matrixNum][int(walker[1])+matrixNum] += float(1.0 / satNum)
    return walkerCount

def Plot2D(classcialWalker,steps):
    plt.figure(1)
    ax1=plt.subplot(111)
    plt.sca(ax1)
    plt.title('2D distribution of %s steps Classical Random Walk' %steps)
    plt.xlabel('X Position(started in center)')
    plt.ylabel('Y Position(started in center)')
    plt.imshow(classcialWalker)
    plt.savefig('Fig/CRW_' + str(steps) + '.png')
    plt.close()

#for i in range(1,2):
#    classicalWalker=classicalRWDistr(i*10,100,100000)
#    Plot2D(classicalWalker,i*10)