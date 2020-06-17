import _thread as thread
from robot import config, logging
from robot.drivers.pixels import pixels
logger = logging.getLogger(__name__)


def wakeup():
    if config.get('/LED/enable', False):
        pixels.wakeup()
    else:
        logger.error('错误：不支持的灯光类型')

def think():
    if config.get('/LED/enable', False):
        pixels.think()
    else:
        logger.error('错误：不支持的灯光类型')

def off():
    if config.get('/LED/enable', False):
        pixels.off()
    else:
        logger.off('错误：不支持的灯光类型')