#!/usr/bin/env python3
# -*- coding: utf-8-*-
# 开源项目地址：https://github.com/wzpan/wukong-robot.git
from snowboy import snowboydecoder
from robot import config, utils, constants, logging, Player
from robot.sdk import LED
from robot.ConfigMonitor import ConfigMonitor
from robot.Conversation import Conversation
from watchdog.observers import Observer
import sys
import os
import fire
import base64
import signal
import random
import hashlib
import urllib3
import requests
import multiprocessing
import _thread as thread
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)


class Xiaobu(object):

    _profiling = False
    _dev = False
    _response_wav = [
        "response1.wav",
        "response2.wav",
        "response3.wav",
        "response4.wav",
        "response5.wav",
    ]
    
    def init(self):
        global conversation
        self.detector = None
        self._thinking = False
        self._interrupted = False        
        config.init()
        self._conversation = Conversation(self._profiling)
        self._conversation.say('你好！我叫小布', True)
        self._observer = Observer()
        event_handler = ConfigMonitor(self._conversation)
        self._observer.schedule(event_handler, constants.CONFIG_PATH, False)
        self._observer.schedule(event_handler, constants.DATA_PATH, False)
        self._observer.start()
        if config.get('/LED/enable', False) and config.get('/LED/type') == 'aiy':
            thread.start_new_thread(self._init_aiy_button_event, ())
        if config.get('/muse/enable', False):
            self._wakeup = multiprocessing.Event()
            self.bci = BCI.MuseBCI(self._wakeup)
            self.bci.start()
            thread.start_new_thread(self._loop_event, ())

    def _loop_event(self):
        while True:
            self._wakeup.wait()
            self._conversation.interrupt()
            query = self._conversation.activeListen()
            self._conversation.doResponse(query)
            self._wakeup.clear()

    def _signal_handler(self, signal, frame):
        self._interrupted = True
        utils.clean()
        self._observer.stop()

    def _detected_callback(self):
        def start_record():
            logger.info('开始录音')    
            print('开始录音') 
            self._conversation.isRecording = True;
        if not utils.is_proper_time():
            logger.warning('勿扰模式开启中')
            return
        if self._conversation.isRecording:
            logger.warning('正在录音中，跳过')
            return
        self._conversation.interrupt()
        if config.get('/LED/enable', False):
            LED.wakeup()
        Player.play(constants.getData(random.choice(self._response_wav)), onCompleted=start_record, wait=True)
        with open("../communication/InPut.txt", "w") as file_writer:
            file_writer.write("true")

    def _do_not_bother_on_callback(self):
        if config.get('/do_not_bother/hotword_switch', False):
            utils.do_not_bother = True
            Player.play(constants.getData('off.wav'))
            logger.info('勿扰模式打开')

    def _do_not_bother_off_callback(self):
        if config.get('/do_not_bother/hotword_switch', False):
            utils.do_not_bother = False
            Player.play(constants.getData('on.wav'))
            logger.info('勿扰模式关闭')

    def _interrupt_callback(self):
        return self._interrupted

    def _init_aiy_button_event(self):
        from aiy.board import Board
        with Board() as board:
            while True:
                board.button.wait_for_press()
                self._conversation.interrupt()
                query = self._conversation.activeListen()
                self._conversation.doResponse(query)

    def run(self):
        self.init()

        # capture SIGINT signal, e.g., Ctrl+C
        signal.signal(signal.SIGINT, self._signal_handler)

        try:
            self.initDetector()
        except AttributeError:
            logger.error('初始化离线唤醒功能失败')
            pass

    def initDetector(self):
        if self.detector is not None:
            self.detector.terminate()
        if config.get('/do_not_bother/hotword_switch', False):
            models = [
                constants.getHotwordModel(config.get('hotword', 'xiaobu.pmdl')),
                constants.getHotwordModel(utils.get_do_not_bother_on_hotword()),
                constants.getHotwordModel(utils.get_do_not_bother_off_hotword())
            ]
        else:
            models = constants.getHotwordModel(config.get('hotword', 'xiaobu.pmdl'))
        self.detector = snowboydecoder.HotwordDetector(models, sensitivity=config.get('sensitivity', 0.5))
        # main loop
        try:
            if config.get('/do_not_bother/hotword_switch', False):
                callbacks = [self._detected_callback,
                             self._do_not_bother_on_callback,
                             self._do_not_bother_off_callback]
            else:
                callbacks = self._detected_callback
            self.detector.start(detected_callback=callbacks,
                                audio_recorder_callback=self._conversation.converse,
                                interrupt_check=self._interrupt_callback,
                                silent_count_threshold=config.get('silent_threshold', 15),
                                recording_timeout=config.get('recording_timeout', 5) * 4,
                                sleep_time=0.03)
            self.detector.terminate()
        except Exception as e:
            logger.critical('离线唤醒机制初始化失败：{}'.format(e))

    def help(self):
        print("""=====================================================================================
    python3 xiaobu.py [命令]
    可选命令：
      train <w1> <w2> <w3> <m> - 传入三个wav文件，生成snowboy的.pmdl模型
                                 w1, w2, w3 表示三个1~3秒的唤醒词录音
                                 m 表示snowboy的.pmdl模型
=====================================================================================""")

    def profiling(self):
        """
        运行过程中打印耗时数据
        """
        logger.info('性能调优')
        self._profiling = True
        self.run()

    def train(self, w1, w2, w3, m):
        '''
        传入三个wav文件，生成snowboy的.pmdl模型
        '''
        def get_wave(fname):
            with open(fname, 'rb') as infile:
                return base64.b64encode(infile.read()).decode('utf-8')
        url = 'https://snowboy.kitt.ai/api/v1/train/'
        data = {
            "name": "xiaobu",
            "language": "zh",
            "token": config.get('snowboy_token', '', True),
            "voice_samples": [
                {"wave": get_wave(w1)},
                {"wave": get_wave(w2)},
                {"wave": get_wave(w3)}
            ]
        }
        response = requests.post(url, json=data)
        if response.ok:
            with open(m, "wb") as outfile:
                outfile.write(response.content)
            return 'Snowboy模型已保存至{}'.format(m)
        else:
            return "Snowboy模型生成失败，原因:{}".format(response.text)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        xiaobu = Xiaobu()
        xiaobu.run()
    elif '-h' in (sys.argv):
        xiaobu = Xiaobu()
        xiaobu.help()
    else:
        fire.Fire(Xiaobu)

