#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'levitan'

from numpy import *
from matplotlib import pyplot as plt
import QWithDiffShift as QDS
import TimebinQuantumWalk as TQW

# distribution=QDS.QWDistribution(1/sqrt(2),1j/sqrt(2),700,1)
# QDS.PlotX(distribution)

def QDSPlot(X0, X1, steps, shiftGateNum, Deg):
    for step in range(1, steps + 1):
        distributionQDS = QDS.QWDistribution(X0, X1, step, shiftGateNum, Deg)
        distributionQW = QDS.QWDistribution(X0, X1, 7 * step, 1, Deg)
        QDS.PlotComp(distributionQDS, distributionQW, step, 'QDS-VS-QW-H')


distributionQDS = QDS.QWDistribution(1 / sqrt(2), 1j / sqrt(2), 10, 3, pi / 3)
distributionQW = QDS.QWDistribution(1 / sqrt(2), 1j / sqrt(2), 7 * 10, 1, pi / 3)
QDS.PlotComp(distributionQDS, distributionQW, 10, 'QDS-VS-QW-60-')

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
#    QDS.QWCicleWithPhaseSearch(1/sqrt(2), 1/sqrt(2), 200, 2, 4, 2*pi*i/50)

# QDS.QWCicleContourfPlot('Data/Search mark_0 X00.707106781187_X10.707106781187_2-4_Steps200Aver.txt', 200, 51,4,2)
# QDS.QWCicleWithPhaseSearch(1, 0, 200, 8, 257, pi)
# QDS.QWFindProbabiltyPlot('Data/search marked 0 2-5.txt',200,5,0)

# TQW.TimebinQW(1, 0, 1, 20, 2, 5,0)
