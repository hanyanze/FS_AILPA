# -*- coding: utf-8-*-
import os
import base64
import tempfile
import pypinyin
from aip import AipSpeech
from . import utils, config, constants
from robot import logging
from pathlib import Path
from pypinyin import lazy_pinyin
from pydub import AudioSegment
from abc import ABCMeta, abstractmethod

logger = logging.getLogger(__name__)

class AbstractTTS(object):
    """
    Generic parent class for all TTS engines
    """

    __metaclass__ = ABCMeta

    @classmethod
    def get_config(cls):
        return {}

    @classmethod
    def get_instance(cls):
        profile = cls.get_config()
        instance = cls(**profile)
        return instance

    @abstractmethod
    def get_speech(self, phrase):
        pass


class BaiduTTS(AbstractTTS):
    """
    使用百度语音合成技术
    要使用本模块, 首先到 yuyin.baidu.com 注册一个开发者账号,
    之后创建一个新应用, 然后在应用管理的"查看key"中获得 API Key 和 Secret Key
    填入 config.yml 中.
    ...
        baidu_yuyin: 
            appid: '9670645'
            api_key: 'qg4haN8b2bGvFtCbBGqhrmZy'
            secret_key: '585d4eccb50d306c401d7df138bb02e7'
            dev_pid: 1936
            per: 1
            lan: 'zh'
        ...
    """

    SLUG = "baidu-tts"

    def __init__(self, appid, api_key, secret_key, per=1, lan='zh', **args):
        super(self.__class__, self).__init__()
        self.client = AipSpeech(appid, api_key, secret_key)
        self.per, self.lan = str(per), lan

    @classmethod
    def get_config(cls):
        # Try to get baidu_yuyin config from config
        return config.get('baidu_yuyin', {})

    def get_speech(self, phrase):
        result  = self.client.synthesis(phrase, self.lan, 1, {'per': self.per});
        # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
        if not isinstance(result, dict):
            tmpfile = utils.write_temp_file(result, '.mp3')
            logger.info('{} 语音合成成功，合成路径：{}'.format(self.SLUG, tmpfile))
            print('{} 语音合成成功，合成路径：{}'.format(self.SLUG, tmpfile))
            return tmpfile
        else:
            logger.critical('{} 合成失败！'.format(self.SLUG), exc_info=True)


def get_engine_by_slug(slug=None):
    """
    Returns:
        A TTS Engine implementation available on the current platform

    Raises:
        ValueError if no speaker implementation is supported on this platform
    """

    if not slug or type(slug) is not str:
        raise TypeError("无效的 TTS slug '%s'", slug)

    selected_engines = list(filter(lambda engine: hasattr(engine, "SLUG") and
                              engine.SLUG == slug, get_engines()))

    if len(selected_engines) == 0:
        raise ValueError("错误：找不到名为 {} 的 TTS 引擎".format(slug))
    else:
        if len(selected_engines) > 1:
            logger.warning("注意: 有多个 TTS 名称与指定的引擎名 {} 匹配").format(slug)        
        engine = selected_engines[0]
        logger.info("使用 {} TTS 引擎".format(engine.SLUG))
        print("使用 {} TTS 引擎".format(engine.SLUG))
        return engine.get_instance()


def get_engines():
    def get_subclasses(cls):
        subclasses = set()
        for subclass in cls.__subclasses__():
            subclasses.add(subclass)
            subclasses.update(get_subclasses(subclass))
        return subclasses
    return [engine for engine in
            list(get_subclasses(AbstractTTS))
            if hasattr(engine, 'SLUG') and engine.SLUG]
