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
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 800, 600))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(50, 50, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(50, 80, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(140, 110, 16, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(160, 80, 71, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 110, 71, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(50, 140, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab)
        self.lineEdit_3.setGeometry(QtCore.QRect(160, 140, 71, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(50, 180, 111, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 180, 71, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(50, 220, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_5 = QtGui.QLineEdit(self.tab)
        self.lineEdit_5.setGeometry(QtCore.QRect(160, 220, 71, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(40, 240, 210, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.tab)
        self.line_2.setGeometry(QtCore.QRect(240, 40, 20, 210))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(40, 260, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.textBrowser = QtGui.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(40, 420, 591, 131))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(40, 400, 91, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line_3 = QtGui.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(40, 30, 210, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(30, 40, 20, 210))
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 260, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 300, 81, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(130, 300, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.mplwidget = MatplotlibWidget(self.tab)
        self.mplwidget.setGeometry(QtCore.QRect(259, 40, 521, 351))
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_Tab2_1 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_1.setGeometry(QtCore.QRect(20, 10, 201, 16))
        self.label_Tab2_1.setObjectName(_fromUtf8("label_Tab2_1"))
        self.label_Tab2_4 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_4.setGeometry(QtCore.QRect(50, 50, 101, 16))
        self.label_Tab2_4.setObjectName(_fromUtf8("label_Tab2_4"))
        self.label_Tab2_3 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_3.setGeometry(QtCore.QRect(50, 80, 101, 16))
        self.label_Tab2_3.setObjectName(_fromUtf8("label_Tab2_3"))
        self.label_Tab2_2 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_2.setGeometry(QtCore.QRect(120, 110, 21, 20))
        self.label_Tab2_2.setObjectName(_fromUtf8("label_Tab2_2"))
        self.label_Tab2_5 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_5.setGeometry(QtCore.QRect(50, 180, 61, 16))
        self.label_Tab2_5.setObjectName(_fromUtf8("label_Tab2_5"))
        self.label_Tab2_6 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_6.setGeometry(QtCore.QRect(50, 220, 121, 20))
        self.label_Tab2_6.setObjectName(_fromUtf8("label_Tab2_6"))
        self.label_Tab2_7 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_7.setGeometry(QtCore.QRect(50, 260, 41, 16))
        self.label_Tab2_7.setObjectName(_fromUtf8("label_Tab2_7"))
        self.label_Tab2_8 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_8.setGeometry(QtCore.QRect(50, 300, 81, 16))
        self.label_Tab2_8.setObjectName(_fromUtf8("label_Tab2_8"))
        self.label_Tab2_9 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_9.setGeometry(QtCore.QRect(50, 340, 81, 16))
        self.label_Tab2_9.setObjectName(_fromUtf8("label_Tab2_9"))
        self.lineEdit__Tab2_1 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit__Tab2_1.setGeometry(QtCore.QRect(170, 80, 61, 20))
        self.lineEdit__Tab2_1.setObjectName(_fromUtf8("lineEdit__Tab2_1"))
        self.lineEdit__Tab2_2 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit__Tab2_2.setGeometry(QtCore.QRect(170, 110, 61, 20))
        self.lineEdit__Tab2_2.setObjectName(_fromUtf8("lineEdit__Tab2_2"))
        self.lineEdit__Tab2_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit__Tab2_3.setGeometry(QtCore.QRect(170, 180, 61, 20))
        self.lineEdit__Tab2_3.setObjectName(_fromUtf8("lineEdit__Tab2_3"))
        self.lineEdit__Tab2_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit__Tab2_4.setGeometry(QtCore.QRect(170, 220, 61, 20))
        self.lineEdit__Tab2_4.setObjectName(_fromUtf8("lineEdit__Tab2_4"))
        self.lineEdit__Tab2_5 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit__Tab2_5.setGeometry(QtCore.QRect(170, 260, 61, 20))
        self.lineEdit__Tab2_5.setObjectName(_fromUtf8("lineEdit__Tab2_5"))
        self.lineEdit__Tab2_6 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit__Tab2_6.setGeometry(QtCore.QRect(170, 300, 61, 20))
        self.lineEdit__Tab2_6.setObjectName(_fromUtf8("lineEdit__Tab2_6"))
        self.lineEdit__Tab2_7 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit__Tab2_7.setGeometry(QtCore.QRect(170, 340, 61, 20))
        self.lineEdit__Tab2_7.setObjectName(_fromUtf8("lineEdit__Tab2_7"))
        self.radioButton_Tab2_1 = QtGui.QRadioButton(self.tab_2)
        self.radioButton_Tab2_1.setGeometry(QtCore.QRect(50, 140, 91, 20))
        self.radioButton_Tab2_1.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton_Tab2_1.setObjectName(_fromUtf8("radioButton_Tab2_1"))
        self.radioButton__Tab2_2 = QtGui.QRadioButton(self.tab_2)
        self.radioButton__Tab2_2.setGeometry(QtCore.QRect(150, 140, 81, 20))
        self.radioButton__Tab2_2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButton__Tab2_2.setObjectName(_fromUtf8("radioButton__Tab2_2"))
        self.label_Tab2_10 = QtGui.QLabel(self.tab_2)
        self.label_Tab2_10.setGeometry(QtCore.QRect(50, 370, 111, 16))
        self.label_Tab2_10.setObjectName(_fromUtf8("label_Tab2_10"))
        self.textBrowser_Tab2__1 = QtGui.QTextBrowser(self.tab_2)
        self.textBrowser_Tab2__1.setGeometry(QtCore.QRect(50, 390, 570, 140))
        self.textBrowser_Tab2__1.setObjectName(_fromUtf8("textBrowser_Tab2__1"))
        self.mplwidget_Tab2_1 = MatplotlibWidget(self.tab_2, hold=True)
        self.mplwidget_Tab2_1.setGeometry(QtCore.QRect(300, 10, 480, 360))
        self.mplwidget_Tab2_1.setObjectName(_fromUtf8("mplwidget_Tab2_1"))
        self.line__Tab2_1 = QtGui.QFrame(self.tab_2)
        self.line__Tab2_1.setGeometry(QtCore.QRect(223, 60, 41, 311))
        self.line__Tab2_1.setFrameShape(QtGui.QFrame.VLine)
        self.line__Tab2_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line__Tab2_1.setObjectName(_fromUtf8("line__Tab2_1"))
        self.pushButton_Tab2_input = QtGui.QPushButton(self.tab_2)
        self.pushButton_Tab2_input.setGeometry(QtCore.QRect(250, 250, 41, 23))
        self.pushButton_Tab2_input.setObjectName(_fromUtf8("pushButton_Tab2_input"))
        self.pushButton__Tab2_run = QtGui.QPushButton(self.tab_2)
        self.pushButton__Tab2_run.setGeometry(QtCore.QRect(250, 280, 41, 23))
        self.pushButton__Tab2_run.setObjectName(_fromUtf8("pushButton__Tab2_run"))
        self.pushButton_Tab2_save = QtGui.QPushButton(self.tab_2)
        self.pushButton_Tab2_save.setGeometry(QtCore.QRect(250, 310, 41, 23))
        self.pushButton_Tab2_save.setObjectName(_fromUtf8("pushButton_Tab2_save"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.paraMeterInput_Tab1)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.walkRun_Tab1)
        QtCore.QObject.connect(self.pushButton_3, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveFig_Tab1)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveData_Tab1)
        QtCore.QObject.connect(self.pushButton_Tab2_input, QtCore.SIGNAL(_fromUtf8("clicked()")),
                               self.paraMeterInput_Tab2)
        QtCore.QObject.connect(self.pushButton__Tab2_run, QtCore.SIGNAL(_fromUtf8("clicked()")), self.walkRun_Tab2)
        QtCore.QObject.connect(self.pushButton_Tab2_save, QtCore.SIGNAL(_fromUtf8("clicked()")), self.saveFig_Tab2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab),
                                  _translate("MainWindow", "Quantum Walk in Line", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2),
                                  _translate("MainWindow", "Quantum Walk in Graph", None))
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
        self.label_Tab2_1.setText(_translate("MainWindow", "Quantum Walk Simulation in Graph", None))
        self.label_Tab2_4.setText(_translate("MainWindow", "Parameter Input:", None))
        self.label_Tab2_3.setText(_translate("MainWindow", "Initial Sate: H", None))
        self.label_Tab2_2.setText(_translate("MainWindow", "  V", None))
        self.label_Tab2_5.setText(_translate("MainWindow", "Walk Step:", None))
        self.label_Tab2_6.setText(_translate("MainWindow", "Shift Gate Number:", None))
        self.label_Tab2_7.setText(_translate("MainWindow", "Node:", None))
        self.label_Tab2_8.setText(_translate("MainWindow", "Mark Phase:", None))
        self.label_Tab2_9.setText(_translate("MainWindow", "Coin Degree:", None))
        self.radioButton_Tab2_1.setText(_translate("MainWindow", "Single Point", None))
        self.radioButton__Tab2_2.setText(_translate("MainWindow", "Aver-Point", None))
        self.label_Tab2_10.setText(_translate("MainWindow", "Result Output:", None))
        self.pushButton_Tab2_input.setText(_translate("MainWindow", "Input", None))
        self.pushButton__Tab2_run.setText(_translate("MainWindow", "Run", None))
        self.pushButton_Tab2_save.setText(_translate("MainWindow", "Save", None))

    def paraMeterInput_Tab1(self):
        self.initStateH = complex(str(self.lineEdit.text()))
        self.initStateV = complex(str(self.lineEdit_2.text()))
        self.walkStep = int(str(self.lineEdit_3.text()))
        self.shiftGateNum = int(str(self.lineEdit_4.text()))
        self.coinDegree = float(int(str(self.lineEdit_5.text())) / 180.0 * pi)
        s = str("initStateH:" + str(self.initStateH) + " initStateV:" + str(self.initStateV) + " walk step:" + str(
            self.walkStep)
                + " Shift Gate:" + str(self.shiftGateNum) + " Coin Degree:" + str(self.coinDegree) + "\n")
        self.textBrowser.append(s)

    def paraMeterInput_Tab2(self):
        self.initStateHTab2 = complex(str(self.lineEdit__Tab2_1.text()))
        self.initStateVTab2 = complex(str(self.lineEdit__Tab2_2.text()))
        self.walkStepTab2 = int(str(self.lineEdit__Tab2_3.text()))
        self.shiftGateNumTab2 = int(str(self.lineEdit__Tab2_4.text()))
        self.nodeTab2 = int(str(self.lineEdit__Tab2_5.text()))
        self.markPhaseTab2 = float(int(str(self.lineEdit__Tab2_6.text())) / 180.0 * pi)
        self.coinDegreeTab2 = float(int(str(self.lineEdit__Tab2_7.text())) / 180.0 * pi)
        if self.radioButton_Tab2_1.isChecked():
            self.isSingle = True
        else:
            self.isSingle = False
        sTab2 = str("Single Point ?: " + str(self.isSingle) + " initStateHTab2:" + str(
            self.initStateHTab2) + " initStateVTab2:" + str(self.initStateVTab2) + " walk step:" + str(
                self.walkStepTab2)
                    + " Shift Gate:" + str(self.shiftGateNumTab2) + " Node:" + str(
            self.nodeTab2) + " Mark Phase:" + str(self.markPhaseTab2) + " Coin Degree:" + str(
            self.coinDegreeTab2) + "\n")
        self.textBrowser_Tab2__1.append(sTab2)

    def walkRun_Tab1(self):
        self.distributionQDS = QDS.QWDistribution(self.initStateH, self.initStateV, self.walkStep, self.shiftGateNum,
                                                  self.coinDegree)
        # print self.distributionQDS
        self.qwPlot_Tab1()

    def walkRun_Tab2(self):
        if self.isSingle is True:
            self.distributionGraphFile = QDS.QWCicleWithPhaseSearchSingle(self.initStateHTab2, self.initStateVTab2,
                                                                          self.walkStepTab2, self.shiftGateNumTab2,
                                                                          self.nodeTab2, self.markPhaseTab2,
                                                                          self.coinDegreeTab2)
            self.textBrowser_Tab2__1.append("Quantum Walk in Graph started in a node\n")
        else:
            self.distributionGraphFile = QDS.QWCicleWithPhaseSearchAver(self.initStateHTab2, self.initStateVTab2,
                                                                        self.walkStepTab2, self.shiftGateNumTab2,
                                                                        self.nodeTab2, self.markPhaseTab2,
                                                                        self.coinDegreeTab2)
            self.textBrowser_Tab2__1.append("Quantum Walk in Graph started in all nodes\n")
        self.mplwidget_Tab2_1.axes.clear()
        fig = self.mplwidget_Tab2_1.axes
        distributionFile = open(self.distributionGraphFile, 'r')
        DataList = zeros([self.nodeTab2, self.walkStepTab2], float)
        for node in range(self.nodeTab2):
            i = 0
            for line in distributionFile.readlines():
                DataList[node][i] = line.split('\t')[node + 2]
                i += 1
            fig.plot(DataList[node])
            distributionFile.seek(0)
            # print DataList[node]
        distributionFile.close()
        fig.set_title("Quantum Walk Simulation in Graph")
        fig.set_xlabel('Step')
        fig.set_ylabel('Probability')
        self.mplwidget_Tab2_1.draw()
        self.textBrowser_Tab2__1.append("Finished plot the distribution !\n")

    def qwPlot_Tab1(self):
        fig = self.mplwidget.axes
        fig.plot(self.distributionQDS)
        fig.set_title("Quantum Walk Simulation")
        fig.set_xlabel('Started from the center')
        fig.set_ylabel('Probability')
        self.mplwidget.draw()
        self.textBrowser.append("Finished plot the distribution !\n")

    def saveFig_Tab1(self):
        self.mplwidget.figure.savefig('Fig/' + "QDS-" + str(self.shiftGateNum) + " " + str(self.walkStep) + '.png')
        self.textBrowser.append("Finished save figure !\n")

    def saveFig_Tab2(self):
        self.mplwidget_Tab2_1.figure.savefig(
            'Fig/' + "QDS-Graph" + str(self.nodeTab2) + " " + str(self.walkStepTab2) + '.png')
        self.textBrowser_Tab2__1.append("Finished save figure !\n")

    def saveData_Tab1(self):
        QDS.writeQWtoArray(self.distributionQDS)
        self.textBrowser.append("Finished save distribution data")


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    f = Ui_MainWindow()
    f.show()
    sys.exit(app.exec_())
