# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
from PyQt5.QtCore import QTimer
import picture
import serial
import serial.tools.list_ports
import threading
import sys
import time
import numpy as np

import process
import usart


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1555, 887)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(1230, 580, 321, 71))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comCB_1 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comCB_1.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.comCB_1.setFont(font)
        self.comCB_1.setObjectName("comCB_1")
        self.horizontalLayout.addWidget(self.comCB_1)
        self.openBtn = QtWidgets.QPushButton(self.layoutWidget_2)
        self.openBtn.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.openBtn.setFont(font)
        self.openBtn.setObjectName("openBtn")
        self.horizontalLayout.addWidget(self.openBtn)
        self.openRad = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.openRad.setMinimumSize(QtCore.QSize(25, 25))
        self.openRad.setMaximumSize(QtCore.QSize(25, 25))
        self.openRad.setText("")
        self.openRad.setIconSize(QtCore.QSize(30, 30))
        self.openRad.setCheckable(False)
        self.openRad.setObjectName("openRad")
        self.horizontalLayout.addWidget(self.openRad)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(1090, 530, 131, 121))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.startBtn.setFont(font)
        self.startBtn.setObjectName("startBtn")
        self.capTestBtn = QtWidgets.QPushButton(self.centralwidget)
        self.capTestBtn.setGeometry(QtCore.QRect(630, 750, 121, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.capTestBtn.setFont(font)
        self.capTestBtn.setObjectName("capTestBtn")
        self.uartTestBtn = QtWidgets.QPushButton(self.centralwidget)
        self.uartTestBtn.setGeometry(QtCore.QRect(630, 660, 121, 81))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.uartTestBtn.setFont(font)
        self.uartTestBtn.setObjectName("uartTestBtn")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(760, 660, 791, 171))
        self.textEdit.setObjectName("textEdit")
        self.label1_2 = QtWidgets.QLabel(self.centralwidget)
        self.label1_2.setGeometry(QtCore.QRect(400, 160, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label1_2.setFont(font)
        self.label1_2.setObjectName("label1_2")
        self.label1_3 = QtWidgets.QLabel(self.centralwidget)
        self.label1_3.setGeometry(QtCore.QRect(780, 160, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label1_3.setFont(font)
        self.label1_3.setObjectName("label1_3")
        self.label1_4 = QtWidgets.QLabel(self.centralwidget)
        self.label1_4.setGeometry(QtCore.QRect(1160, 160, 191, 121))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label1_4.setFont(font)
        self.label1_4.setObjectName("label1_4")
        self.label1 = QtWidgets.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(20, 170, 171, 111))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(72)
        font.setBold(False)
        font.setWeight(50)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(410, 300, 351, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.surface4 = QtWidgets.QLabel(self.layoutWidget)
        self.surface4.setMinimumSize(QtCore.QSize(161, 0))
        self.surface4.setMaximumSize(QtCore.QSize(161, 161))
        self.surface4.setObjectName("surface4")
        self.gridLayout_3.addWidget(self.surface4, 0, 2, 1, 1)
        self.surface3 = QtWidgets.QLabel(self.layoutWidget)
        self.surface3.setMinimumSize(QtCore.QSize(161, 0))
        self.surface3.setMaximumSize(QtCore.QSize(161, 161))
        self.surface3.setObjectName("surface3")
        self.gridLayout_3.addWidget(self.surface3, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 1, 1, 1)
        self.surface5 = QtWidgets.QLabel(self.centralwidget)
        self.surface5.setGeometry(QtCore.QRect(910, 310, 161, 161))
        self.surface5.setMaximumSize(QtCore.QSize(161, 161))
        self.surface5.setObjectName("surface5")
        self.surface6 = QtWidgets.QLabel(self.centralwidget)
        self.surface6.setGeometry(QtCore.QRect(1290, 310, 161, 161))
        self.surface6.setMaximumSize(QtCore.QSize(161, 161))
        self.surface6.setObjectName("surface6")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 11, 1531, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_ld = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ld.setMaximumSize(QtCore.QSize(640, 480))
        self.label_ld.setText("")
        self.label_ld.setObjectName("label_ld")
        self.gridLayout.addWidget(self.label_ld, 0, 3, 1, 1)
        self.label_rd = QtWidgets.QLabel(self.layoutWidget1)
        self.label_rd.setMaximumSize(QtCore.QSize(640, 16777215))
        self.label_rd.setText("")
        self.label_rd.setObjectName("label_rd")
        self.gridLayout.addWidget(self.label_rd, 0, 4, 1, 1)
        self.label_ru = QtWidgets.QLabel(self.layoutWidget1)
        self.label_ru.setMaximumSize(QtCore.QSize(640, 480))
        self.label_ru.setText("")
        self.label_ru.setObjectName("label_ru")
        self.gridLayout.addWidget(self.label_ru, 0, 1, 1, 1)
        self.label_lu = QtWidgets.QLabel(self.layoutWidget1)
        self.label_lu.setMaximumSize(QtCore.QSize(640, 480))
        self.label_lu.setText("")
        self.label_lu.setObjectName("label_lu")
        self.gridLayout.addWidget(self.label_lu, 0, 2, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(30, 300, 351, 181))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.surface2 = QtWidgets.QLabel(self.layoutWidget2)
        self.surface2.setMinimumSize(QtCore.QSize(161, 161))
        self.surface2.setMaximumSize(QtCore.QSize(161, 161))
        self.surface2.setObjectName("surface2")
        self.gridLayout_2.addWidget(self.surface2, 0, 2, 1, 1)
        self.surface1 = QtWidgets.QLabel(self.layoutWidget2)
        self.surface1.setMinimumSize(QtCore.QSize(161, 0))
        self.surface1.setMaximumSize(QtCore.QSize(161, 161))
        self.surface1.setObjectName("surface1")
        self.gridLayout_2.addWidget(self.surface1, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 1, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 640, 591, 191))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 10, 571, 171))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout_4.addWidget(self.label_5, 0, 4, 1, 1)
        self.SminSld = QtWidgets.QSlider(self.layoutWidget3)
        self.SminSld.setMinimumSize(QtCore.QSize(175, 0))
        self.SminSld.setMaximumSize(QtCore.QSize(175, 16777215))
        self.SminSld.setMaximum(255)
        self.SminSld.setProperty("value", 0)
        self.SminSld.setOrientation(QtCore.Qt.Horizontal)
        self.SminSld.setObjectName("SminSld")
        self.gridLayout_4.addWidget(self.SminSld, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 2, 0, 1, 1)
        self.VmaxNum = QtWidgets.QLineEdit(self.layoutWidget3)
        self.VmaxNum.setMaximumSize(QtCore.QSize(30, 16777215))
        self.VmaxNum.setObjectName("VmaxNum")
        self.gridLayout_4.addWidget(self.VmaxNum, 3, 5, 1, 1)
        self.HmaxNum = QtWidgets.QLineEdit(self.layoutWidget3)
        self.HmaxNum.setMaximumSize(QtCore.QSize(30, 16777215))
        self.HmaxNum.setObjectName("HmaxNum")
        self.gridLayout_4.addWidget(self.HmaxNum, 1, 5, 1, 1)
        self.SmaxNum = QtWidgets.QLineEdit(self.layoutWidget3)
        self.SmaxNum.setMaximumSize(QtCore.QSize(30, 16777215))
        self.SmaxNum.setObjectName("SmaxNum")
        self.gridLayout_4.addWidget(self.SmaxNum, 2, 5, 1, 1)
        self.VminNum = QtWidgets.QLineEdit(self.layoutWidget3)
        self.VminNum.setMaximumSize(QtCore.QSize(30, 16777215))
        self.VminNum.setObjectName("VminNum")
        self.gridLayout_4.addWidget(self.VminNum, 3, 2, 1, 1)
        self.HminNum = QtWidgets.QLineEdit(self.layoutWidget3)
        self.HminNum.setMaximumSize(QtCore.QSize(30, 16777215))
        self.HminNum.setText("")
        self.HminNum.setObjectName("HminNum")
        self.gridLayout_4.addWidget(self.HminNum, 1, 2, 1, 1)
        self.VmaxSld = QtWidgets.QSlider(self.layoutWidget3)
        self.VmaxSld.setMaximumSize(QtCore.QSize(175, 16777215))
        self.VmaxSld.setMaximum(255)
        self.VmaxSld.setProperty("value", 0)
        self.VmaxSld.setOrientation(QtCore.Qt.Horizontal)
        self.VmaxSld.setObjectName("VmaxSld")
        self.gridLayout_4.addWidget(self.VmaxSld, 3, 4, 1, 1)
        self.HminSld = QtWidgets.QSlider(self.layoutWidget3)
        self.HminSld.setMinimumSize(QtCore.QSize(175, 0))
        self.HminSld.setMaximumSize(QtCore.QSize(175, 16777215))
        self.HminSld.setMaximum(255)
        self.HminSld.setProperty("value", 0)
        self.HminSld.setOrientation(QtCore.Qt.Horizontal)
        self.HminSld.setObjectName("HminSld")
        self.gridLayout_4.addWidget(self.HminSld, 1, 1, 1, 1)
        self.SminNum = QtWidgets.QLineEdit(self.layoutWidget3)
        self.SminNum.setMaximumSize(QtCore.QSize(30, 16777215))
        self.SminNum.setObjectName("SminNum")
        self.gridLayout_4.addWidget(self.SminNum, 2, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_4.addWidget(self.label_4, 0, 1, 1, 1)
        self.VminSld = QtWidgets.QSlider(self.layoutWidget3)
        self.VminSld.setMinimumSize(QtCore.QSize(175, 0))
        self.VminSld.setMaximumSize(QtCore.QSize(175, 16777215))
        self.VminSld.setMaximum(255)
        self.VminSld.setProperty("value", 0)
        self.VminSld.setOrientation(QtCore.Qt.Horizontal)
        self.VminSld.setObjectName("VminSld")
        self.gridLayout_4.addWidget(self.VminSld, 3, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 0, 1, 1)
        self.HmaxSld = QtWidgets.QSlider(self.layoutWidget3)
        self.HmaxSld.setMinimumSize(QtCore.QSize(175, 0))
        self.HmaxSld.setMaximumSize(QtCore.QSize(175, 16777215))
        self.HmaxSld.setMaximum(255)
        self.HmaxSld.setProperty("value", 0)
        self.HmaxSld.setOrientation(QtCore.Qt.Horizontal)
        self.HmaxSld.setObjectName("HmaxSld")
        self.gridLayout_4.addWidget(self.HmaxSld, 1, 4, 1, 1)
        self.SmaxSld = QtWidgets.QSlider(self.layoutWidget3)
        self.SmaxSld.setMinimumSize(QtCore.QSize(175, 0))
        self.SmaxSld.setMaximumSize(QtCore.QSize(175, 16777215))
        self.SmaxSld.setMaximum(255)
        self.SmaxSld.setProperty("value", 0)
        self.SmaxSld.setOrientation(QtCore.Qt.Horizontal)
        self.SmaxSld.setObjectName("SmaxSld")
        self.gridLayout_4.addWidget(self.SmaxSld, 2, 4, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1555, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.mySetup()

    def mySetup(self):
        # 槽函数
        self.startBtn.clicked.connect(self.start)
        self.openBtn.clicked.connect(self.open)
        self.capTestBtn.clicked.connect(self.capTest)
        self.uartTestBtn.clicked.connect(self.uartTest__)

        self.HminSld.valueChanged.connect(lambda: self.sliderValueChanged("H", 0))
        self.SminSld.valueChanged.connect(lambda: self.sliderValueChanged("S", 0))
        self.VminSld.valueChanged.connect(lambda: self.sliderValueChanged("V", 0))

        self.HmaxSld.valueChanged.connect(lambda: self.sliderValueChanged("H", 1))
        self.SmaxSld.valueChanged.connect(lambda: self.sliderValueChanged("S", 1))
        self.VmaxSld.valueChanged.connect(lambda: self.sliderValueChanged("V", 1))

        # 其他初始化
        threadAutoSearch = threading.Thread(name='th1', target=self.serailAutoSearch)
        threadAutoSearch.start()
        self.com = usart.serialMain()
        self.openflag = 0

        self.label_rd.setText(" ")
        self.label_ld.setText(" ")
        self.label_lu.setText(" ")
        self.label_ru.setText(" ")

        self.side = [['', '', ''],
                     ['', '', ''],
                     ['', '', '']]
        self.cube = {"U": [['', '', ''], ['', '', ''], ['', '', '']],
                     "L": [['', '', ''], ['', '', ''], ['', '', '']],
                     "F": [['', '', ''], ['', '', ''], ['', '', '']],
                     "R": [['', '', ''], ['', '', ''], ['', '', '']],
                     "B": [['', '', ''], ['', '', ''], ['', '', '']],
                     "D": [['', '', ''], ['', '', ''], ['', '', '']]}

        self.color = [0, 0, 0, 0, 0, 0]

        # 定时器初始化
        self.CapTimer = QTimer()
        self.CapTimer.timeout.connect(self.capevent)
        self.CapTimer.start(100)

        # 视频流初始化
        self.cap1 = cv2.VideoCapture(1)
        self.cap2 = cv2.VideoCapture(2)
        self.cap3 = cv2.VideoCapture(3)
        self.cap4 = cv2.VideoCapture(4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openBtn.setText(_translate("MainWindow", "打开"))
        self.startBtn.setText(_translate("MainWindow", "开始还原"))
        self.capTestBtn.setText(_translate("MainWindow", "摄像头测试"))
        self.uartTestBtn.setText(_translate("MainWindow", "串口连接测试"))
        self.label1_2.setText(_translate("MainWindow", ""))
        self.label1_3.setText(_translate("MainWindow", ""))
        self.label1_4.setText(_translate("MainWindow", ""))
        self.label1.setText(_translate("MainWindow", ""))
        self.surface4.setText(_translate("MainWindow", "TextLabel"))
        self.surface3.setText(_translate("MainWindow", "TextLabel"))
        self.surface5.setText(_translate("MainWindow", "TextLabel"))
        self.surface6.setText(_translate("MainWindow", "TextLabel"))
        self.surface2.setText(_translate("MainWindow", "TextLabel"))
        self.surface1.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "V:"))
        self.label_2.setText(_translate("MainWindow", "S:"))
        self.label_5.setText(_translate("MainWindow", "Max"))
        self.label.setText(_translate("MainWindow", "H:"))
        self.label_4.setText(_translate("MainWindow", "Min"))


    def capshow(self, cap, label):
        if cap.isOpened():
            # start = time.perf_counter()
            ret, image_ = cap.read()
            image = cv2.resize(image_, (384, 288))  # 把读到的帧的大小重新设置为 640x480
            # ---------------------------------
            # 在这里添加代码
            # ----------------------------------
            process.findColor(image, self.color)
            # ----------------------------------
            show = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # 视频色彩转换回RGB，这样才是现实的颜色

            showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],
                                    QtGui.QImage.Format_RGB888)  # 把读取到的视频数据变成QImage形式
            label.setPixmap(QtGui.QPixmap.fromImage(showImage))  # 往显示视频的Label里 显示QImage

            # end = time.perf_counter()
            # print(end - start)
        return 0

    def capdetect(self, capnum, cap):



        return 0


    def sliderValueChanged(self, hsv, flag):
        """
        功能描述：获取滑动条的值并设置 XxxxNum的显示值
        接口：hsv 值为“H” “S" "V"
             flag 值为 0/1 0为选中min 1为max
        修改记录：2023-4-1   创建函数
        """
        mm = "max" if flag else "min"
        value = self.__dict__[str(hsv) + str(mm) + "Sld"].value()
        self.__dict__[str(hsv) + str(mm) + "Num"].setText(str(value))

        self.color[0] = self.HminSld.value()
        self.color[1] = self.SminSld.value()
        self.color[2] = self.VminSld.value()

        self.color[3] = self.HmaxSld.value()
        self.color[4] = self.SmaxSld.value()
        self.color[5] = self.VmaxSld.value()
        print(self.color)
        return 0

    def capevent(self):
        """
        功能描述：在label中显示摄像头获取的图像，由self.CapTimer = QTimer()的timeout调用
        接口：None
        修改记录：2023-4-1   创建函数
        """
        self.capshow(self.cap1, self.label_lu)
        self.capshow(self.cap2, self.label_ru)
        self.capshow(self.cap3, self.label_ld)
        self.capshow(self.cap4, self.label_rd)
        return 0

    def printui(self, str):
        """
        功能描述：将发送给下位机的数据显示到界面中，并加上时间戳
        接口：str 要发送的字符串
        修改记录：2023-4-1   创建函数
        """
        time_stamp = time.strftime("[%m-%d %H:%M:%S]", time.localtime())
        self.textEdit.append(time_stamp + " " + str)

    def serailAutoSearch(self):
        """
        功能描述：一个用于自动搜索串口的进程
        接口：None
        修改记录：2023-4-1
        """
        while True:
            ports = list(serial.tools.list_ports.comports(include_links=True))
            self.comCB_1.clear()
            for port in ports:
                com = "{} {}".format(port.device, port.description)
                self.comCB_1.addItem(com)
                # print(port)

    def open(self):
        """
        功能描述：打开串口
        接口：None
        修改记录：2023-4-1   创建函数
        """
        if self.openflag == 0:
            self.openflag = 1
            port = self.comCB_1.currentText().split(" ")[0]
            if port == "":
                return -1
            else:
                self.openBtn.setText("关闭")
                print("open")
                self.openRad.setStyleSheet("QRadioButton::indicator {width:14px;height:14px;border-radius:7px}"
                                     "QRadioButton::indicator {background-color:red;}")
                self.com.init(port)
                self.com.open()
        elif self.openflag == 1:
            self.openflag = 0
            self.com.close()
            self.openBtn.setText("打开")
            self.openRad.setStyleSheet("")

    def start(self):
        """
        功能描述：摄像头读取一帧，识别颜色，然后调用kociemba算法，获取解传给下位机
        接口：None
        修改记录：2023-4-1   创建函数
        """
        print("start")



    def capTest(self):
        # self.printui("<--CAPTEST-->")
        """
        功能描述：
                标志摄像头，用于确定摄像头顺序，会创建threadAuotShutDown进程，等待3s将标识取消
        接口：None
        修改记录：2023-4-1   创建函数
        """
        _translate = QtCore.QCoreApplication.translate
        self.label1.setText(_translate("MainWindow", " 1 "))
        self.label1.setStyleSheet("background:rgb(20,20,20);color:rgb(240,240,240)")
        self.label1_3.setText(_translate("MainWindow", " 3 "))
        self.label1_3.setStyleSheet("background:rgb(20,20,20);color:rgb(240,240,240)")
        self.label1_4.setText(_translate("MainWindow", " 4 "))
        self.label1_4.setStyleSheet("background:rgb(20,20,20);color:rgb(240,240,240)")
        self.label1_2.setText(_translate("MainWindow", " 2 "))
        self.label1_2.setStyleSheet("background:rgb(20,20,20);color:rgb(240,240,240)")

        threadAutoShutdown = threading.Thread(name='th1', target=self.capTestThreading)
        threadAutoShutdown.start()

    def capTestThreading(self):
        time.sleep(3)
        _translate = QtCore.QCoreApplication.translate
        self.label1.setText(_translate("MainWindow", ""))
        self.label1.setStyleSheet("")
        self.label1_3.setText(_translate("MainWindow", ""))
        self.label1_3.setStyleSheet("")
        self.label1_4.setText(_translate("MainWindow", ""))
        self.label1_4.setStyleSheet("")
        self.label1_2.setText(_translate("MainWindow", ""))
        self.label1_2.setStyleSheet("")
        return 0

    def uartTest__(self):
        # self.printui("<--UARTTEST-->")

        return 0

