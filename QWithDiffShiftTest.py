#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'levitan'

from numpy import *
from matplotlib import pyplot as plt
import QWithDiffShift as QDS


# distribution=QDS.QWDistribution(1/sqrt(2),1j/sqrt(2),700,1)
# QDS.PlotX(distribution)

def QDSPlot(X0, X1, steps, shiftGateNum):
    for step in range(1, steps + 1):
        distributionQDS = QDS.QWDistribution(X0, X1, step, shiftGateNum)
        distributionQW = QDS.QWDistribution(X0, X1, 7 * step, 1)
        QDS.PlotComp(distributionQDS, distributionQW, step, 'QDS-VS-QW-H')


def QDSCPlot(X0, X1, steps, shiftGateNum, node):
    for step in range(1, steps + 1):
        distribution = QDS.QWCicleDistribution(X0, X1, step, shiftGateNum, node)
        distributionTrans = QDS.ciclePosiTrans(distribution, step, shiftGateNum)
        QDS.PlotX(distributionTrans, step, 'QDS_CT')

# QDSPlot(1/sqrt(2),1j/sqrt(2),15,3)
# QDSCPlot(1/sqrt(2),1j/sqrt(2),15,3,50)

def QDSCiclePlot(X0, X1, steps, shiftGateNum, node):
    for step in range(1, steps + 1):
        distribution = QDS.QWCicleDistribution(X0, X1, step, shiftGateNum, node)
        distributionTrans = QDS.ciclePosiTrans(distribution, step, shiftGateNum)
        QDS.PlotCicle(distributionTrans, step, shiftGateNum, 'QDSCicle_K4_H_')


def QDSCicleContourfPlot(Filename, walkSteps, PiSteps, node, point):
    # x,y=ogrid[0:50:PiSteps,1:200:walkSteps]
    x = arange(0, 2 * pi, 2 * pi / PiSteps)
    y = arange(0, walkSteps, 1)
    v = linspace(0, 1, 50, endpoint=True)
    # print x,shape(x)
    file = open(Filename, 'r')
    dataList = zeros([walkSteps * PiSteps, node])
    i = 0
    for line in file.readlines():
        for j in range(node):
            dataList[i][j] = line.split('\t')[2 + j]
        # print dataList[i]
        i += 1
    # print dataList[2]
    z = zeros([walkSteps, PiSteps], float)
    for yi in range(walkSteps):
        for xi in range(PiSteps):
            z[yi][xi] = float(dataList[xi * walkSteps + yi][point])
    file.close()
    plt.figure()
    plt.title('Distribution of %s steps Quantum Walk in Cicle with different phase' % walkSteps)
    plt.xlabel('Phase')
    plt.ylabel('Step')
    plt.contourf(x, y, z, v, cmap=plt.cm.jet)
    x = plt.colorbar(ticks=v)
    print x
    plt.show()


# QDSCiclePlot(1, 0, 10, 2, 4)
# QDSPlot(1 , 0, 10, 3)
# QDS.QWCicleDistrWrite(1, 0, 2000, 3, 8)
# QDS.QWCicleWithPhaseDistrWrite(1/sqrt(2), 1/sqrt(2), 400, 2, 5, 0, 2)
# QDS.QWCicleWithPhaseLoopDistrWrite(1/sqrt(2), 1j/sqrt(2), 200, 2, 4, pi, 2)
# QDS.QWCicleWithPhaseLoopSearch(1/sqrt(2), 1/sqrt(2), 200, 3, 8, pi, 3)

# for i in range(51):
#     QDS.QWCicleWithPhaseLoopSearch(1, 0, 200, 3, 8, 2*pi*i/50, 3)

# for i in range(51):
#     QDS.QWCicleWithPhaseLoopDistrWritePosi(1/sqrt(2), 1/sqrt(2), 200, 2, 4, 2*pi*i/50, 2)

# for i in range(51):
#    QDS.QWCicleWithPhaseDistrWrite(1/sqrt(2), 1/sqrt(2), 200, 2, 5, 2*pi*i/50, 2)

# for i in range(51):
#    QDS.QWCicleWithPhaseSearch(1/sqrt(2), 1/sqrt(2), 200, 2, 4, 2*pi*i/50, 2)

QDSCicleContourfPlot('Data/Search mark_0 X00.707106781187_X10.707106781187_2-4_Steps200Aver.txt', 200, 51,4,2)
