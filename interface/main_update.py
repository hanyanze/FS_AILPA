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
                os.system('chmod 777 /home/pi/FS_AILPA/run_file/*.sh')
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

    def _get_content(self, path, current):
        if os.path.exists(os.path.join(path, 'CONTENT')):
            with open(os.path.join(path, 'CONTENT'), 'r') as f:
                return f.read().strip()
        else:
            return current

    def _put_content(self, path, content):
        if os.path.exists(os.path.join(path, 'CONTENT')):
            with open(os.path.join(path, 'CONTENT'), 'w') as f:
                return f.write(content)
        else:
            pass

    def fetch(self):
        global URL
        url = URL
        try:
            r = requests.get(url, timeout=3)
            info = json.loads(r.text)
            main_version = info['tag_name']
            # 检查主仓库
            current_main_version = self._get_version(APP_PATH, main_version)
            if semver.compare(main_version, current_main_version) > 0:
                print('主仓库检查到更新：{}'.format(info['tag_name']))
                self.update_info['tag_name'] = info['tag_name']
            if 'body' in info:
                self.update_info['body'] = info['body']
                self._put_content(APP_PATH, self.update_info['body'])
            return self.update_info
        except Exception as e:
            print("检查更新失败：", e)
            return {"error": "检查更新失败，请稍后再试！"}


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.u = Updater()
        self.update_info = {}
        self.label.setText("当前版本：" + self.u._get_version(APP_PATH, "未知"))
        self.textEdit.setText(self.u._get_content(APP_PATH, "未知"))
        self.pushButton_min.setStyleSheet("QPushButton{border-image: url(images/min.png)}")
        self.pushButton_close.setStyleSheet("QPushButton{border-image: url(images/close.png)}")

    def checkupdate(self, item):
        if self.pushButton.text() == "检查更新":
            self.pushButton.setEnabled(False)
            self.update_info = self.u.fetch()
            # print(self.update_info)
            try:
                if 'tag_name' in self.update_info:
                    self.textEdit.setText(self.update_info['body'])
                    self.pushButton.setEnabled(True)
                    self.pushButton.setText("更新")
                elif 'error' in self.update_info:
                    self.textEdit.setText(self.update_info['error'])
                    self.pushButton.setEnabled(True)
                else:
                    self.textEdit.setText("已经是最新版本啦~~~")
                    self.pushButton.setEnabled(True)
            except Exception as e:
                print(e)
        elif self.pushButton.text() == "更新":
            self.pushButton.setEnabled(False)
            self.pushButton.setText("更新失败")
            if self.u.update(self.update_info):
                self.label.setText("当前版本：" + self.u._get_version(APP_PATH, "未知"))
                self.pushButton.setText("更新成功!")
                self.pushButton.setEnabled(True)
                self.update_info.clear()

    @staticmethod
    def display_min():
        MainWindow.showMinimized()

    def display_close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = MyWindow()
    # showFullScreen()
    # MainWindow.setWindowFlags(FramelessWindowHint)
    MainWindow.show()
    sys.exit(app.exec_())




