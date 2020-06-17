# -*- coding: utf-8 -*-
# author = hyz
import sys
import time
from test_find_friend import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random
from getIP.getip import *
from find_friend.myudp import *
import os
import json
import signal
import threading


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.timer_check_network = QTimer(self)
        self.timer_check_network.timeout.connect(self.getip)
        self.timer_check_network.start(30)
        self.t1 = threading.Thread(target=my_udp.receivemsg)
        self.t1.start()
        self.ipList = []
        self.friend = ""
        self.ip = get.Getip()

    def getip(self):
        _ipList = []
        if my_udp.recvmsg != "":
            dictDeviceIp = json.loads(my_udp.recvmsg)
            for i in dictDeviceIp.keys():
                if (i == "deviceip") and (dictDeviceIp[i] not in self.ipList):
                    self.ipList.append(dictDeviceIp[i])
                    self.listWidget.clear()
                    for j in self.ipList:
                        self.listWidget.addItem(j)
                if i == "devicestatus":
                    QMessageBox.information(self, "连接状态", "连接成功")
            my_udp.recvmsg = ""

    def find_x(self):
        my_udp.sendmsg_broadcast(json.dumps({"xiaobu": "online"}), 15678)

    def connect(self):
        my_udp.sendmsg_unicast(json.dumps({"xiaobuip": self.ip}), self.friend, 15678)

    def getItem(self, item):
        self.friend = self.listWidget.item(item.row()).text()

    def display_min(self):
        MainWindow.showMinimized()

    def display_close(self):
        self.t1.stop()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.showFullScreen()
    MainWindow.show()
    sys.exit(app.exec_())




