#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'levitan'

import quantumRW as QW
from numpy import *
from matplotlib import pyplot as plt

totalSteps=100
plotSteps=10
# steps=50
# qwalker= QW.distriQW(1/sqrt(2),1j/sqrt(2),1/sqrt(2),1j/sqrt(2),steps,1)

#QW.Plot2D(qwalker)
#QW.PlotX(qwalker,steps)
#QW.writeQW(qwalker,'QW_'+str(steps)+'.txt')


qwalker=QW.quantumWalker(1/sqrt(2),1j/sqrt(2),1/sqrt(2),1j/sqrt(2),totalSteps,plotSteps)