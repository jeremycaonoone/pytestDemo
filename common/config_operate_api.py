#coding=utf-8
import os
from configparser import ConfigParser


class Dictionary(dict):
    '''
    把config.ini中的参数添加值dict
    '''
    def __getattr__(self, keyname):
        #如果key值不存在则返回默认值"not find config keyname"
        return self.get(keyname, "config.ini中没有找到对应的keyname")

class Config(object):
    '''
    ConfigParser二次封装，在字典中获取value
    '''
    def __init__(self):
        # 设置配置文件路径
        current_dir = os.path.dirname(__file__)
        top_one_dir = os.path.dirname(current_dir)
        file_name = top_one_dir + "/conf/config.ini"
        # 实例化ConfigParser对象
        self.config = ConfigParser()
        self.config.read(file_name,encoding="utf-8")
        #根据section把key、value写入字典
        for section in self.config.sections():
            setattr(self, section, Dictionary())
            for keyname, value in self.config.items(section):
                setattr(getattr(self, section), keyname, value)

    def getconf(self, section):
        '''
        用法：
        conf = Config()
        info = conf.getconf("main").url
        '''
        if section in self.config.sections():
            pass
        else:
            print(" 找不到该 section")
        return getattr(self, section)
