# -*- coding: utf-8-*-
import os
from robot import config, logging
from robot.Player import MusicPlayer
from robot.sdk.AbstractPlugin import AbstractPlugin

logger = logging.getLogger(__name__)

class Plugin(AbstractPlugin):

    IS_IMMERSIVE = True  # 这是个沉浸式技能

    def __init__(self, con):
        super(Plugin, self).__init__(con)
        self.player = None
        self.song_list = None

    def get_song_list(self, path):
        if not os.path.exists(path) or not os.path.isdir(path):
            return []
        song_list = list(filter(lambda d: d.endswith('.mp3'), os.listdir(path)))
        return [os.path.join(path, song) for song in song_list]

    def init_music_player(self):
        self.song_list = self.get_song_list(config.get('/LocalPlayer/path'))
        if self.song_list == None:
            logger.error('{} 插件配置有误'.format(self.SLUG))
        logger.info('本地音乐列表：{}'.format(self.song_list))
        print('本地音乐列表：{}'.format(self.song_list))
        return MusicPlayer(self.song_list, self)

    def handle(self, text, parsed):
        if any(word in text for word in ['音乐', '歌']):
            if not self.player:
                self.player = self.init_music_player()
            if len(self.song_list) == 0:
                self.clearImmersive()  # 去掉沉浸式
                self.say('本地音乐目录并没有音乐文件，播放失败')
                return
            self.player.play()
        elif any(word in text for word in ['下', '换']):
            self.player.next()
        elif any(word in text for word in ['上']):
            self.player.prev()
        elif any(word in text for word in ['大']):
            self.player.turnUp()
        elif any(word in text for word in ['小']):
            self.player.turnDown()
        elif any(word in text for word in ['暂停']):
            self.player.pause()
        elif any(word in text for word in ['继续']):
            self.player.resume()
        elif any(word in text for word in ['关闭', '停止']):
            self.player.stop()
            self.clearImmersive()  # 去掉沉浸式
        else:
            self.say('没听懂你的意思呢，要停止播放，请说停止播放', wait=True)
            self.player.resume()

    def pause(self):
        if self.player:
            self.player.stop()

    def restore(self):
        if self.player and not self.player.is_pausing():
            self.player.resume()

    def isValidImmersive(self, text, parsed):
        return any(word in text for word in ['播放', '下', '换', '上', '大', '小', '暂停', '关闭', '停止'])

    def isValid(self, text, parsed):
        return any(word in text for word in ['播放音乐', '听歌'])