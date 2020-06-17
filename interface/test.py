# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(804, 485)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 480))
        self.label_2.setStyleSheet("QLabel{\n"
"    background-image: url(\'./images/back.png\');\n"
"}")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 430, 411, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("QLabel{\n"
"background:rgba(0, 0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"")
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 100, 471, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(22)
        self.label_7.setFont(font)
        self.label_7.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_7.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_7.setStyleSheet("QLabel{\n"
"background:rgba(0, 0, 0, 0);\n"
"color:rgb(255, 255, 255)\n"
"}")
        self.label_7.setObjectName("label_7")
        self.label_sound = QtWidgets.QLabel(self.centralwidget)
        self.label_sound.setGeometry(QtCore.QRect(570, 340, 162, 71))
        self.label_sound.setStyleSheet("QLabel{\n"
"    background:rgba(255, 255, 255, 0);\n"
"}")
        self.label_sound.setText("")
        self.label_sound.setObjectName("label_sound")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    border:1px solid #B3B3B3;\n"
"    border-radius:15px;\n"
"    background:rgba(200, 200, 200, 0.6);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    border:1px solid #B3B3B3;\n"
"    border-radius:15px;\n"
"    background:rgba(200, 200, 200, 0.6);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 270, 301, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("QLineEdit{\n"
"    border:1px solid #B3B3B3;\n"
"    border-radius:15px;\n"
"    background:rgba(200, 200, 200, 0.6);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(400, 270, 331, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("QLineEdit{\n"
"    border:1px solid #B3B3B3;\n"
"    border-radius:15px;\n"
"    background:rgba(200, 200, 200, 0.6);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(540, 190, 191, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("QLineEdit{\n"
"    border:1px solid #B3B3B3;\n"
"    border-radius:15px;\n"
"    background:rgba(200, 200, 200, 0.6);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lcd = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd.setGeometry(QtCore.QRect(610, 100, 121, 41))
        self.lcd.setStyleSheet("")
        self.lcd.setObjectName("lcd")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(60, 350, 481, 51))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(20)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    border:1px solid #B3B3B3;\n"
"    border-radius:15px;\n"
"    background:rgba(200, 200, 200, 0.6);\n"
"    color:rgb(255, 255, 255)\n"
"}")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
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
        self.label_2.raise_()
        self.label_7.raise_()
        self.label_sound.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_4.raise_()
        self.lcd.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.display_min)
        self.pushButton_2.clicked.connect(MainWindow.display_close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "想和我聊天，试着对我说：小布小布"))
        self.lineEdit.setText(_translate("MainWindow", " 几点了"))
        self.lineEdit_2.setText(_translate("MainWindow", " 把灯打开"))
        self.lineEdit_3.setText(_translate("MainWindow", " 空气温湿度是多少"))
        self.lineEdit_5.setText(_translate("MainWindow", " 家里光照强度是多少"))
        self.lineEdit_4.setText(_translate("MainWindow", " 把窗帘打开"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:20pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))

