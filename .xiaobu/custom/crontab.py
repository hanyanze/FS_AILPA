# -*- coding: utf-8-*-
import os
import re
import time
from datetime import datetime
from robot.sdk.AbstractPlugin import AbstractPlugin
from apscheduler.schedulers.background import BackgroundScheduler


class Plugin(AbstractPlugin):
    timeChinese = {
    "六十":60, "五十九":59, "五十八":58, "五十七":57, "五十六":56, "五十五":55, "五十四":54, "五十三":53, "五十二":52, "五十一":51, 
    "五十":50, "四十九":49, "四十八":48, "四十七":47, "四十六":46, "四十五":45, "四十四":44, "四十三":43, "四十二":42, "四十一":41, 
    "四十":40, "三十九":39, "三十八":38, "三十七":37, "三十六":36, "三十五":35, "三十四":34, "三十三":33, "三十二":32, "三十一":31, 
    "三十":30, "二十九":29, "二十八":28, "二十七":27, "二十六":26, "二十五":25, "二十四":24, "二十三":23 ,"二十二":22, "二十一":21, 
    "二十":20, "十九":19, "十八":18, "十七":17, "十六":16, "十五":15, "十四":14, "十三":13, "十二":12, "十一":11, 
    "十":10, "九":9, "八":8, "七":7, "六":6, "五":5, "四":4, "三":3, "两":2, "二":2, "一":1, "零":0, "半":30, "整":0}

    def tick(self):
        # print('Tick! The time is: %s' % datetime.now())
        timeNow = time.strftime("%H-%M", time.localtime()).split("-")
        self.say('现在时间是{}点{}分'.format(timeNow[0], timeNow[1]), cache=True)

    def filter_time(self, text):
        timeArabic = text
        if any(word in text for word in [u"点"]) and any(word in text for word in [u"定"]):
            try:
                for i in self.timeChinese.keys():
                    try:
                        timeArabic = timeArabic.replace(i, str(self.timeChinese[i]))
                    except Exception as e:
                        print(e)
                findTime = re.findall(r"(.*?)点(.*)", timeArabic)
                timeList = re.findall(r'\d+', findTime[0][0])
                hour = int(timeList[len(timeList) - 1])
                timeList = re.findall(r'\d+', findTime[0][1])
                minute = int(timeList[0])
                if int(hour) > 23 or minute > 60 or hour < 0 or minute < 0:
                    return -1, -1
                return hour, minute
            except Exception as e:
                return -1, -1
        elif any(word in text for word in [u"定"]):
            try:
                timeArabic = re.findall('\d+',timeArabic)
                hour = timeArabic[0][:-2]
                minute = timeArabic[0][-2:]
                return hour, minute
            except Exception as e:
                return -1, -1
        else:
            return -1, -1

    def handle(self, text, parsed):
        try:
            hour, minute = self.filter_time(text)
            if hour != -1:
                self.say('闹钟设定到{}点{}分!'.format(str(hour), str(minute)), cache=True)
                scheduler = BackgroundScheduler()
                scheduler.add_job(self.tick, 'cron', hour=hour, minute=minute)
                scheduler.start()
            else:
                self.say('闹钟设定失败', cache=True)
        except Exception as e:
            print("error:", e)

    def isValid(self, text, parsed):
        return any(word in text for word in [u"闹钟"])
