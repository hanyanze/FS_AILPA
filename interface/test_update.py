# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test_update.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 371)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_close = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_close.setGeometry(QtCore.QRect(720, 20, 50, 50))
        self.pushButton_close.setText("")
        self.pushButton_close.setObjectName("pushButton_close")
        self.pushButton_min = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_min.setGeometry(QtCore.QRect(640, 10, 64, 64))
        self.pushButton_min.setText("")
        self.pushButton_min.setObjectName("pushButton_min")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 20, 531, 331))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(580, 130, 201, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 220, 201, 131))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 795, 370))
        self.label_2.setStyleSheet("QLabel{\n"
"    background-image: url(\\\'./images/back.png\\\');\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.pushButton_close.raise_()
        self.pushButton_min.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_min.clicked.connect(MainWindow.display_min)
        self.pushButton_close.clicked.connect(MainWindow.display_close)
        self.pushButton.clicked.connect(MainWindow.checkupdate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "当前版本：未知"))
        self.pushButton.setText(_translate("MainWindow", "检查更新"))

