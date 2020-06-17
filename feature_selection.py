#!/usr/bin/env python3
import os
import sys
import time
import signal

def sh_process_info(process_name):
        command = "ps aux | grep " + process_name
        out = os.popen(command).read()
        for line in out.splitlines():
            print(line)
            if "sh " + process_name in line:
                pid = int(line.split()[1])
                print("pid = ", pid)
                return pid, True
        return 1, False

def py_process_info(process_name):
        command = "ps aux | grep " + process_name
        out = os.popen(command).read()
        for line in out.splitlines():
            if "python3 " + process_name in line:
                pid = int(line.split()[1])
                return pid, True
        return 1, False

def process_info_stop(processId):
    try:
        os.kill(processId, signal.SIGKILL)
        # print('已杀死pid为%s的进程,　返回值是:%s' % (processId, a))
    except OSError:
        # print('没有如此进程!!!')
        return False
    return True


if __name__ == "__main__":
    print('''****************************
    (1)开启语音助手
    (2)开启语音界面
    (3)开启传感器控制
    (4)训练唤醒词
    (5)修改配置文件
    (6)退出
****************************''')
    status = input("输入：")
    if status == "1":
        os.system("cd ./xiaobu && python3 xiaobu.py")
    elif status == "2":
        os.system("cd ./interface && python3 main.py")
    elif status == "3":
        os.system("cd ./interface && python3 main_hass.py")
    elif status == "4":
        num = 4
        i = 1
        name = input("输入训练模型名称：")
        if name != "":
            while i < num:
                print("开始录音......")
                path = "test{}.wav".format(i)
                os.system("cd ./xiaobu/train/ && python3 recoder.py " + path + " > /dev/null 2>&1")
                status = input("完成录音,是否保存并继续y/n,默认y:")
                if status == "n":
                    os.system("rm ./xiaobu/train/" + path)
                    i -= 1
                    print("已删除上一录音,2秒后开始录音")
                i += 1
                if i < num:
                    print("已保存,2秒后开始录音")
                else:
                    print("已保存,2秒后开始训练")
                time.sleep(2)
            print("开始训练")
            os.system("cd ./xiaobu && python3 xiaobu.py train ./train/test1.wav ./train/test2.wav ./train/test3.wav ../.xiaobu/" + name + ".pmdl")
    elif status == "5":
        os.system("vim .xiaobu/config.yml")
    elif status == "6":
        pass
    else:
        pass
