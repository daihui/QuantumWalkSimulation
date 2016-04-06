#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'levitan'

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy import *
import QWithDiffShift as QDS
import time


class AnimatedScatterQW(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""

    def __init__(self, X0, X1, steps, shiftGateNum, node):
        self.X0 = X0
        self.X1 = X1
        self.steps = steps
        self.shiftGateNum = shiftGateNum
        self.node = node
        self.step = 1
        self.linedata = zeros([self.node, 1])
        self.distri = self.distribution()

        # Setup the figure and axes...
        self.fig = plt.figure()
        self.ax1 = plt.subplot(211)
        plt.title('Quantum Walk in Cycle Graph,view in cycle')
        self.step_text1 = self.ax1.text(-1.8, 1.2, '')
        self.step_text1.set_text('')
        self.ax2 = plt.subplot(212)
        # self.ax2_axis=self.ax2.axis([1, self.node, 0, 1])
        # self.ax2_axis.set_axis()
        plt.title('Quantum Walk in Cycle Graph,position 0 probability')
        # plt.title('Quantum Walk in Cycle Graph,position probability by step')
        # Then setup FuncAnimation.
        self.ani = animation.FuncAnimation(self.fig, self.update, frames=200, interval=500,
                                           init_func=self.setup_plot, blit=True)

    def setup_plot(self):
        """Initial drawing of the scatter plot."""
        data = next(self.distri)
        # temp=array([data[:,2]]).T
        # print temp
        # self.linedata=column_stack((self.linedata,temp))
        # print self.linedata
        x = data[:, 0]
        y = data[:, 1]
        d = data[:, 2]
        self.ax1.axis([-4.5, 4.5, -1.5, 1.5])
        self.scat = self.ax1.scatter(x, y, s=d, c='red', marker='o', animated=True)

        self.ax2.axis([1, 100, 0, 1])
        self.line, = self.ax2.plot([], [])
        # For FuncAnimation's sake, we need to return the artist we'll be using
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat, self.line,

    def distribution(self):
        """Generate a quantum walk distribution in Cycle Graph . """
        step = 1
        radius = 1
        node = self.node
        data = zeros([node, 3], float)
        Filename = 'Data/' + time.strftime('%Y%m%d-%H-%M-%S') + '.txt'
        distrFlie = open(Filename, 'w+')
        for j in range(node):
            data[j, 0] = sin(j * 2 * math.pi / node) * radius
            data[j, 1] = cos(j * 2 * math.pi / node) * radius
        while True:
            distribution = QDS.QWCicleDistribution(self.X0, self.X1, step, self.shiftGateNum, node)
            # data[:,2]= QDS.ciclePosiTrans(distribution, step, node)
            data[:, 2] = distribution
            # write distribution to txt file
            distrFlie.write(str(step) + '\t')
            for x in range(shape(distribution)[0]):
                distrFlie.write(str(distribution[x]) + '\t')
            distrFlie.write('\n')
            self.step = step
            print ('step: %s') % step
            step += 1
            yield data
        distrFlie.close()

    def update(self, i):
        """Update the scatter plot."""
        data = next(self.distri)
        # Set x and y data...
        temp = array([data[:, 2]]).T
        # print temp
        self.linedata = column_stack((self.linedata, temp))
        m, n = shape(self.linedata)
        # print self.linedata
        self.scat.set_offsets(data[:, :2])
        # self.line.set_offsets(data[:,:2])
        # Set sizes...
        self.scat._sizes = data[:, 2] * 200
        # self.line._sizes = data[:,2]*500
        lineResize = self.linedata.copy()
        lineResize.resize(1, self.step)
        # print lineResize[0]
        x = arange(1, self.step + 1)
        y = lineResize[0]
        # print x,y
        self.line.set_data(x, y)

        self.step_text1.set_text('Setp:%s' % self.step)
        # self.ax2.axis([1, self.step, 0, 1])
        # self.ax2_axis.set_axis([[1, self.step, 0, 1]])
        # self.scat.set_title(self.Title)
        # Set colors..
        # self.scat.set_array(data[3])

        # We need to return the updated artist for FuncAnimation to draw..
        # Note that it expects a sequence of artists, thus the trailing comma.
        return self.scat, self.line, self.step_text1,

    def show(self):
        plt.show()


if __name__ == '__main__':
    a = AnimatedScatterQW(1, 0, 100, 3, 8)
    a.show()
