# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Python Project\QuantumWalkSimulation\QuantumWalkGUI.ui'
#
# Created: Tue Jun 14 17:03:44 2016
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlibwidget import MatplotlibWidget
import sys
from numpy import *
import QWithDiffShift as QDS

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8


    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
        self.initStateH = complex(1)
        self.initStateV = complex(0)
        self.walkStep = 10
        self.shiftGateNum = 3
        self.coinDegree = float(45 / 180.0 * pi)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 110, 16, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(160, 80, 71, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 110, 71, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 140, 71, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(50, 180, 111, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 180, 71, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(50, 220, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_5 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 220, 71, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(40, 240, 201, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(230, 40, 20, 211))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 260, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(40, 420, 591, 131))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(40, 400, 91, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(40, 30, 201, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(30, 40, 20, 211))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 300, 81, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 300, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.mplwidget = MatplotlibWidget(self.centralwidget)
        self.mplwidget.setGeometry(QtCore.QRect(259, 40, 521, 351))
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.paraMeterInput)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.walkRun)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveFig)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveData)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Quantum Walk Simulation for Different Shift ", None))
        self.label_2.setText(_translate("MainWindow", "Parameter Input:", None))
        self.label_3.setText(_translate("MainWindow", "Initial State: H", None))
        self.label_4.setText(_translate("MainWindow", "V", None))
        self.label_5.setText(_translate("MainWindow", "Walk Step:", None))
        self.label_6.setText(_translate("MainWindow", "Shift Gate Number:", None))
        self.label_7.setText(_translate("MainWindow", "Coin Degree:", None))
        self.pushButton.setText(_translate("MainWindow", "Input", None))
        self.label_8.setText(_translate("MainWindow", "Result Output:", None))
        self.pushButton_2.setText(_translate("MainWindow", "Run", None))
        self.pushButton_3.setText(_translate("MainWindow", "Save Picture", None))
        self.pushButton_4.setText(_translate("MainWindow", "Save Data", None))

    def paraMeterInput(self):
        self.initStateH = complex(str(self.lineEdit.text()))
        self.initStateV = complex(str(self.lineEdit_2.text()))
        self.walkStep = int(str(self.lineEdit_3.text()))
        self.shiftGateNum = int(str(self.lineEdit_4.text()))
        self.coinDegree = float(int(str(self.lineEdit_5.text())) / 180.0 * pi)
        s = str("initStateH:" + str(self.initStateH) + " initStateV:" + str(self.initStateV) + " walk step:" + str(
            self.walkStep)
                + " Shift Gate:" + str(self.shiftGateNum) + " Coin Degree:" + str(self.coinDegree) + "\n")
        self.textBrowser.append(s)

    def walkRun(self):
        self.distributionQDS = QDS.QWDistribution(self.initStateH, self.initStateV, self.walkStep, self.shiftGateNum,
                                                  self.coinDegree)
        # print self.distributionQDS
        self.qwPlot()

    def qwPlot(self):
        fig = self.mplwidget.axes
        fig.plot(self.distributionQDS)
        fig.set_title("Quantum Walk Simulation")
        fig.set_xlabel('Started from the center')
        fig.set_ylabel('Probability')
        self.mplwidget.draw()
        self.textBrowser.append("Finished plot the distribution !\n")

    def saveFig(self):
        self.mplwidget.figure.savefig('Fig/' + "QDS-" + str(self.shiftGateNum) + " " + str(self.walkStep) + '.png')
        self.textBrowser.append("Finished save figure !\n")

    def saveData(self):
        QDS.writeQWtoArray(self.distributionQDS)
        self.textBrowser.append("Finished save distribution data")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    f = Ui_MainWindow()
    f.show()
    sys.exit(app.exec_())
