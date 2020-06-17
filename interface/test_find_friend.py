# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_find_friend.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label_2.setStyleSheet("QLabel{\n"
"    background-image: url(\'./images/back.png\');\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_sound = QtWidgets.QLabel(self.centralwidget)
        self.label_sound.setGeometry(QtCore.QRect(570, 340, 162, 71))
        self.label_sound.setStyleSheet("QLabel{\n"
"    background:rgba(255, 255, 255, 0);\n"
"}")
        self.label_sound.setText("")
        self.label_sound.setObjectName("label_sound")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 20, 50, 50))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    border: 0px solid rgba(0, 0, 0, 0); \n"
"    background:rgba(0, 0, 0, 0);\n"
"    focus{padding: -1;};\n"
"    border-image: url(images/min.png);\n"
"}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(730, 30, 41, 40))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    border: 0px solid rgba(0, 0, 0, 0); \n"
"    background:rgba(0, 0, 0, 0);\n"
"    focus{padding: -1;};\n"
"    border-image: url(images/close.png);\n"
"}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 40, 421, 421))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(500, 240, 271, 101))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(500, 360, 271, 101))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.display_min)
        self.pushButton_2.clicked.connect(MainWindow.display_close)
        self.pushButton_3.clicked.connect(MainWindow.find_x)
        self.pushButton_4.clicked.connect(MainWindow.connect)
        self.listWidget.clicked['QModelIndex'].connect(MainWindow.getItem)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_3.setText(_translate("MainWindow", "找朋友"))
        self.pushButton_4.setText(_translate("MainWindow", "连接该朋友"))

