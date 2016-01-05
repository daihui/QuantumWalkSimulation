#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'levitan'
import math
from numpy import *
import numpy as np
import random
from matplotlib import pyplot as plt


def classicalRanNum():
    coinX = int(random.choice(['1', '-1']))
    coinY = int(random.choice(['1', '-1']))
    return coinX, coinY


# print classicalRanNum()

def classicalWalkerPosition():
    positionX = 0
    positionY = 0
    return positionX, positionY


def classicalWalk(walkNum):
    walkerPositionX, walkerPositionY = classicalWalkerPosition()
    for i in range(0, walkNum):
        coinX, coinY = classicalRanNum()
        walkerPositionX += coinX
        walkerPositionY += coinY
    return walkerPositionX, walkerPositionY


def classicalRWDistr(walkNum, matrixNum,satNum):
   # positionList = []
    walkerCount = zeros([2 *matrixNum + 1, 2 * matrixNum + 1])
    for i in range(0, satNum):
        walker = classicalWalk(walkNum)
        #print walker,walker[0],walker[1]
       # positionList.append(walker)
        walkerCount[walker[0]+matrixNum][walker[1]+matrixNum] += float(1.0 / satNum)
    return walkerCount

def Plot2D(classcialWalker,steps):
    plt.figure(1)
    ax1=plt.subplot(111)
    plt.sca(ax1)
    plt.title('2D distribution of %s steps Classical Random Walk' %steps)
    plt.xlabel('X Position(started in center)')
    plt.ylabel('Y Position(started in center)')
    plt.imshow(classcialWalker)
    plt.savefig('CRW_'+str(steps)+'.png')
    plt.close()

for i in range(1,11):
    classicalWalker=classicalRWDistr(i*10,100,100000)
    Plot2D(classicalWalker,i*10)