# -*- coding: utf-8 -*-
# author = hyz
# 这是“系统更新”的界面
import os
import sys
import json
import semver
import requests
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from subprocess import call
from PyQt5.QtWidgets import *
from test_update import Ui_MainWindow
from datetime import datetime, timedelta

APP_PATH = "/home/pi/FS_AILPA/"
_updater = None
URL = 'https://api.github.com/repos/hanyanze/FS_AILPA/releases/latest'


class Updater(object):
    def __init__(self):
        self.last_check = datetime.now() - timedelta(days=1.5)
        self.update_info = {}

    def _pull(self, cwd, tag):
        if os.path.exists(cwd):
            return call(['git checkout master && git pull && git checkout {}'.format(tag)], cwd=cwd, shell=True) == 0
        else:
            print("目录 {} 不存在".format(cwd))
            return False

    def _pip(self, cwd):
        if os.path.exists(cwd):
            return call(['pip3', 'install', '-r', 'requirements.txt'], cwd=cwd, shell=False) == 0
        else:
            print("目录 {} 不存在".format(cwd))
            return False

    def update(self, update_info):
        # update_info = self.fetch()
        # print(update_info)
        success = True
        if 'tag_name' in update_info:
            if self._pull(APP_PATH, update_info['tag_name']) and self._pip(APP_PATH):
                self.update_info.clear()
                print('更新成功！')
            else:
                print('更新失败！')
                success = False
        return success

    def _get_version(self, path, current):
        if os.path.exists(os.path.join(path, 'VERSION')):
            with open(os.path.join(path, 'VERSION'), 'r') as f:
                return f.read().strip()
        else:
            return current

    def fetch(self, dev=False):
        global URL
        url = URL
        try:
            r = requests.get(url, timeout=3)
            info = json.loads(r.text)
            main_version = info['tag_name']
            # 检查主仓库
            current_main_version = self._get_version(APP_PATH, main_version)
            print(current_main_version)
            if semver.compare(main_version, current_main_version) > 0:
                print('主仓库检查到更新：{}'.format(info['tag_name']))
                self.update_info['tag_name'] = info['tag_name']
            if 'body' in info:
                self.update_info['body'] = info['body']
            return self.update_info
        except Exception as e:
            print("检查更新失败：", e)
            return {"error": "检查更新失败，请稍后再试！"}


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.u = Updater()
        self.update_info = {}
        self.label.setText("当前版本：" + self.u._get_version(APP_PATH, "未知"))

    def checkupdate(self, item):
        if self.pushButton.text() == "检查更新":
            self.update_info = self.u.fetch()
            print(self.update_info)
            try:
                if 'tag_name' in self.update_info:
                    print("aaaa")
                    self.textEdit.setText(self.update_info['body'])
                    self.pushButton.setText("更新")
                elif 'error' in self.update_info:
                    print("bbbb")
                    self.textEdit.setText(self.update_info['error'])
                else:
                    print("cccc")
                    self.textEdit.setText("已经是最新版本啦~~~")
            except Exception as e:
                pass
        elif self.pushButton.text() == "更新":
            if self.u.update(self.update_info):
                self.textEdit.setText(self.update_info['body'])
                self.pushButton.setText("检查更新")

    @staticmethod
    def display_min():
        MainWindow.showMinimized()

    def display_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    MainWindow.showFullScreen()
    MainWindow.show()
    sys.exit(app.exec_())




