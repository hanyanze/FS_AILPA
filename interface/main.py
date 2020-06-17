# -*- coding: utf-8 -*-
# author = hyz
# 这是“语音界面”的界面
import sys
import time
from test import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
from getIP.getip import *
import os
import signal
import threading


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.initUI()
        self.pic_num = 0
        self.out1 = ""
        self.in1 = ""
        self.timer_check_network = QTimer(self)
        self.timer_check_network.timeout.connect(self.ping)
        self.timer_check_network.start(1000)
        self.timer_language = QTimer(self)
        self.timer_language.timeout.connect(self.display_language)
        self.timer_language.start(200)
        self.timer_display_recording = QTimer(self)
        self.timer_display_recording.timeout.connect(self.display_recording)
        self.label_sound.setStyleSheet(
            "background:rgba(0, 0, 0, 0);background-image: url(./images/images/image1.png);")
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.start()
        self.timer.timeout.connect(self.update_time)
        self.first_open = True
        with open("../communication/OutPut.txt", "r+") as file_writer:
            file_writer.truncate()
        with open("../communication/InPut.txt", "r+") as file_writer:
            file_writer.truncate()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.DATA_POSITION = 22
        self.picNum = 89
        self.last_read = "false"

    def initUI(self):
        self.setWindowTitle('小布音响')
        self.lcd.setMode(QLCDNumber.Dec)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setStyleSheet("border: 0px;color:rgb(255, 255, 255);background:rgba(0, 0, 0, 0);")
        hour, minute, second = time.strftime("%X", time.localtime()).split(":")
        self.lcd.display(hour + ":" + minute)

    def update_time(self):
        hour, minute, second = time.strftime("%X", time.localtime()).split(":")
        self.lcd.display(hour + ":" + minute)

    @staticmethod
    def isNetOK(testserver):
        s = socket.socket()
        s.settimeout(3)
        try:
            status = s.connect_ex(testserver)
            if status == 0:
                s.close()
                return True
            else:
                return False
        except Exception as e:
            return False

    def ping(self):
        isOK = self.isNetOK(testserver=('www.baidu.com', 443))
        # print(isOK)
        if isOK:
            ip = get.Getip()
            self.label.setText("IP地址：" + ip)
        else:
            self.label.setText("网络故障")

    def display_language(self):
        try:
            with open("../communication/OutPut.txt", "r") as file_writer2:
                read_in = file_writer2.read()[2:-2]
                self.textEdit.clear()
                self.textEdit.setText(read_in)
        except:
            pass
        try:
            with open("../communication/InPut.txt", "r") as file_writer2:
                read_in = file_writer2.read()
                if read_in == "true" and self.last_read != "true":
                    self.timer_display_recording.start(33)
                elif read_in == "false" and self.last_read == "true":
                    self.label_sound.setStyleSheet("background-color:rgb(255, 255, 255);")
                    self.timer_display_recording.stop()
                    self.label_sound.setStyleSheet(
                        "background:rgba(0, 0, 0, 0);background-image: url(./images/images/image1.png);")
                else:
                    pass
                self.last_read = read_in
        except:
            pass

    def display_recording(self):
        self.picNum += 1
        if self.picNum >= 150:
            self.picNum = 18
        self.label_sound.setStyleSheet("background-image: url(./images/images/image{}.png);".format(self.picNum))


    def display_min(self):
        MainWindow.showMinimized()

    def display_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.showFullScreen()
    MainWindow.show()
    sys.exit(app.exec_())




