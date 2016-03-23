#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'levitan'

from numpy import *
import QWithDiffShift as QDS


# distribution=QDS.QWDistribution(1/sqrt(2),1j/sqrt(2),700,1)
# QDS.PlotX(distribution)

def QDSPlot(X0, X1, steps, shiftGateNum):
    for step in range(1, steps + 1):
        distributionQDS = QDS.QWDistribution(X0, X1, step, shiftGateNum)
        distributionQW = QDS.QWDistribution(X0, X1, 7 * step, 1)
        QDS.PlotComp(distributionQDS, distributionQW, step)


def QDSCPlot(X0, X1, steps, shiftGateNum, node):
    for step in range(1, steps + 1):
        distribution = QDS.QWDistribution(X0, X1, step, shiftGateNum, node)
        distributionTrans = QDS.ciclePosiTrans(distribution, step, shiftGateNum)
        QDS.PlotX(distributionTrans, step, 'QDS_CT')

# QDSPlot(1/sqrt(2),1j/sqrt(2),15,3)
# QDSCPlot(1/sqrt(2),1j/sqrt(2),15,3,50)

def QDSCiclePlot(X0, X1, steps, shiftGateNum, node):
    for step in range(1, steps + 1):
        distribution = QDS.QWDistribution(X0, X1, step, shiftGateNum, node)
        distributionTrans = QDS.ciclePosiTrans(distribution, step, shiftGateNum)
        QDS.PlotCicle(distributionTrans, step, shiftGateNum, 'QDSCicle_K9_')


QDSCiclePlot(1 / sqrt(2), 1j / sqrt(2), 25, 3, 9)
