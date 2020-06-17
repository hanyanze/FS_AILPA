# -*- coding: utf-8-*-
import yaml
import logging
import os

_config = {}
has_init = False

def doInit(config_file="/home/pi/xiaobu-smartHome/local_socket/config.yml"):
    global _config
    dict_num = 0
    # Read config
    try:
        with open(config_file, "r") as f:
            _config = yaml.safe_load(f)
            dict_num = len(_config.keys())
    except Exception as e:
        print("配置文件 {} 读取失败: {}".format(config_file, e))
        raise
    return dict_num


def get_path(items, default=None, warm=False):
    global _config
    curConfig = _config
    if isinstance(items, str) and items[0] == '/':
        items = items.split('/')[1:]
    for key in items:
        if key in curConfig:
            curConfig = curConfig[key]
        else:
            if warm:
                print("/%s not specified in profile, defaulting to "
                             "'%s'", '/'.join(items), default)
            else:
                print("/%s not specified in profile, defaulting to "
                             "'%s'", '/'.join(items), default)
            return default
    return curConfig


def has_path(items):
    global _config
    curConfig = _config
    if isinstance(items, str) and items[0] == '/':
        items = items.split('/')[1:]
    else:
        items = [items]
    for key in items:
        if key in curConfig:
            curConfig = curConfig[key]
        else:
            return False
    return True


def get(item='', default=None, warm=False):
    """
    获取某个配置的值
    :param item: 配置项名。如果是多级配置，则以 "/a/b" 的形式提供
    :param default: 默认值（可选）
    :param warm: 不存在该配置时，是否告警
    :returns: 这个配置的值。如果没有该配置，则提供一个默认值
    """
    if not item:
        return _config
    if item[0] == '/':
        return get_path(item, default, warm)
    try:
        return _config[item]
    except KeyError:
        if warm:
           print("%s not specified in profile, defaulting to '%s'",
                         item, default)
        else:
            print("%s not specified in profile, defaulting to '%s'",
                         item, default)
        return default
