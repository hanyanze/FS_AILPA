# -*- coding: utf-8-*-
from robot.Player import MusicPlayer
from robot import logging
from robot.sdk.AbstractPlugin import AbstractPlugin

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):
    def __init__(self, con):
        super(Plugin, self).__init__(con)
        self.player = None

    def handle(self, text, parsed):
        try:
            if not self.player:
                self.player = MusicPlayer([], self)
            if any(word in text for word in ['大']):
                self.player.turnUp()
            elif any(word in text for word in ['小']):
                self.player.turnDown()
            else:
                self.say('请下达调整音量的指令。', cache=True)
        except Exception as e:
            print(e)

    def isValid(self, text, parsed):
        return any(word in text for word in ['声音', '音量'])

