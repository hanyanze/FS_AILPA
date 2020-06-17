# -*- coding: utf-8-*-
from robot.sdk.AbstractPlugin import AbstractPlugin
import datetime

class Plugin(AbstractPlugin):
    def handle(self, text, parsed):
        try:
            nowTime = datetime.datetime.now().strftime('%H-%M')
            self.say('现在是{}点{}分'.format(nowTime.split("-")[0], nowTime.split("-")[1]), cache=True)
        except Exception as e:
            self.say('获取时间失败', cache=True)

    def isValid(self, text, parsed):
        return any(word in text for word in [u"几点"])
