# -*- coding: utf-8-*-
import json
from aip import AipSpeech
from .sdk import BaiduSpeech
from . import utils, config, constants
from robot import logging
from abc import ABCMeta, abstractmethod

logger = logging.getLogger(__name__)

class AbstractASR(object):
    """
    Generic parent class for all ASR engines
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
    def transcribe(self, fp):
        pass


class BaiduASR(AbstractASR):
    """
    百度的语音识别API.
    dev_pid:
        - 1936: 普通话远场
        - 1536：普通话(支持简单的英文识别)
        - 1537：普通话(纯中文识别)
        - 1737：英语
        - 1637：粤语
        - 1837：四川话
    要使用本模块, 首先到 yuyin.baidu.com 注册一个开发者账号,
    之后创建一个新应用, 然后在应用管理的"查看key"中获得 API Key 和 Secret Key
    填入 config.xml 中.
    """

    SLUG = "baidu-asr"

    def __init__(self, appid, api_key, secret_key, dev_pid=1936, **args):
        super(self.__class__, self).__init__()
        if dev_pid != 80001:
            self.client = AipSpeech(appid, api_key, secret_key)
        else:
            self.client = BaiduSpeech.baiduSpeech(api_key, secret_key, dev_pid)
        self.dev_pid = dev_pid

    @classmethod
    def get_config(cls):
        # Try to get baidu_yuyin config from config
        return config.get('baidu_yuyin', {})

    def transcribe(self, fp):
        # 识别本地文件
        pcm = utils.get_pcm_from_wav(fp)
        res = self.client.asr(pcm, 'pcm', 16000, {
            'dev_pid': self.dev_pid,
        })
        if res['err_no'] == 0:
            logger.info('{} 语音识别到了：{}'.format(self.SLUG, res['result']))
            print('{} 语音识别到了：{}'.format(self.SLUG, res['result']))
            with open("../communication/OutPut.txt","w") as file_writer:
                file_writer.write(str(res['result']))
            return ''.join(res['result'])
        else:
            logger.info('{} 语音识别出错了: {}'.format(self.SLUG, res['err_msg']))
            print('{} 语音识别出错了: {}'.format(self.SLUG, res['err_msg']))
            return ''


def get_engine_by_slug(slug=None):
    """
    Returns:
        An ASR Engine implementation available on the current platform

    Raises:
        ValueError if no speaker implementation is supported on this platform
    """

    if not slug or type(slug) is not str:
        raise TypeError("无效的 ASR slug '%s'", slug)

    selected_engines = list(filter(lambda engine: hasattr(engine, "SLUG") and
                              engine.SLUG == slug, get_engines()))

    if len(selected_engines) == 0:
        raise ValueError("错误：找不到名为 {} 的 ASR 引擎".format(slug))
    else:
        if len(selected_engines) > 1:
            logger.warning("注意: 有多个 ASR 名称与指定的引擎名 {} 匹配").format(slug)
        engine = selected_engines[0]
        logger.info("使用 {} ASR 引擎".format(engine.SLUG))
        print("使用 {} ASR 引擎".format(engine.SLUG))
        return engine.get_instance()


def get_engines():
    def get_subclasses(cls):
        subclasses = set()
        for subclass in cls.__subclasses__():
            subclasses.add(subclass)
            subclasses.update(get_subclasses(subclass))
        return subclasses
    return [engine for engine in
            list(get_subclasses(AbstractASR))
            if hasattr(engine, 'SLUG') and engine.SLUG]
