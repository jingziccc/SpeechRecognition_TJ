# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'asrInterface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.window_width = 500
        self.window_height = 700
        self.label_width = self.window_width * (4 / 5)
        self.label_height = self.window_height / 10

        MainWindow.resize(self.window_width, self.window_height)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)

        # 按钮控件设置
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(self.window_width / 2 - 60, self.window_height - 100, 120, 40))
        self.pushButton.setText("Start Listening")
        self.pushButton.setFont(font)
        self.pushButton.pressed.connect(self.start_listening)
        self.pushButton.released.connect(self.stop_listening)
        self.pushButton.setStyleSheet("background-color: rgb(173, 216, 230);")
        # label控件设置
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 250, 201, 21))
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.labels = [self.label_2, self.label_3, self.label_4, self.label_5]

        self.voiceFig = QtWidgets.QLabel(self.centralwidget)
        self.voiceFig.setGeometry(QtCore.QRect(self.window_width / 2 - 130, 0, 100, 121))
        self.voiceFig.setText("")
        self.gif = QMovie("icon/voice.gif")
        self.voiceFig.setMovie(self.gif)
        self.gif.start()
        self.voiceFig.setFixedSize(self.gif.frameRect().size() / 2.5)
        self.voiceFig.setScaledContents(True)
        self.voiceFig.setObjectName("voiceFig")

        for idx, label in enumerate(self.labels):
            label.setGeometry(QtCore.QRect(60, 280 + idx * 70, self.label_width, 50))
            label.setFont(font)
            label.setStyleSheet("color: rgb(0, 117, 210);")
            label.setWordWrap(True)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(self.window_width / 2 - 120,  (self.window_height - self.label_height) / 8 + 80, self.label_width, 60))
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 117, 210);")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Voice Assistant"))
        self.label_3.setText(_translate("MainWindow", "1. Play music by saying \"Play music\""))
        self.label_2.setText(_translate("MainWindow", "You can:"))
        self.label.setText(_translate("MainWindow", "Hi! How can I help?"))
        self.label_4.setText(_translate("MainWindow", "2. Take some notes by saying \"Open Notepad\""))
        self.label_5.setText(_translate("MainWindow", " "))

    def start_listening(self):
        # 在这里编写开始录音的代码
        print("开始录音")

    def stop_listening(self):
        # 在这里编写停止录音的代码
        print("停止录音")

