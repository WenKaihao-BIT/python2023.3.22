# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo8.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from pyqtgraph import PlotWidget
import sys,cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import numpy as np
import pyqtgraph as pq
from ClassSer import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = PlotWidget(self.centralwidget)




        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.data1 = np.array([0])
        # self.data2 = np.random.normal(size=300)

        self.curve1 = self.graphicsView.plot(self.data1, name="mode2",pen=pq.mkPen(color='b',width=2))
        # self.curve2 = self.graphicsView.plot(self.data2, name="mode1")

        ##设置样式
        self.graphicsView.setBackground('w')


        # 设定定时器
        self.timer = pq.QtCore.QTimer()
        # 定时器信号绑定 update_data 函数
        self.timer.timeout.connect(self.update_data)
        # 定时器间隔50ms，可以理解为 50ms 刷新一次数据
        self.timer.start(50)

        self.ser = serial_port()


    def update_data(self):
        self.ser.receivedata()
        self.data = self.ser.receive
        if self.data:
            self.data = float(self.data)
            print(self.data)
            if len(self.data1) < 100:
                self.curve1.setData(self.data1)
                self.data1 = np.append(self.data1, self.data)
                print(len(self.data1))
                print(self.data1)
            else:
                self.data1[:-1] = self.data1[1:]
                self.data1[-1] = self.data
                # 数据填充到绘制曲线中
                self.curve1.setData(self.data1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
# from pyqtgraph import PlotWidget
if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())