#coding=utf-8
import logging
from common.public_path import DIR
import time
import os


def get_log(logger_name):
    """

    :param logger_name: 填项目名称表示哪个项目
    :return:
    """

    #创建一个logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    #获取本地时间，转换为设置的格式
    #rq = time.strftime('%Y%m%d%H%M',time.localtime(time.time()))
    rq = time.strftime("%Y_%m_%d_")
    #设置日志文件存放路径，日志文件名

    #设置所有日志和错误日志的存放路径
    # 通过getcwd.py文件的绝对路径来拼接日志存放路径
    all_log_path = os.path.join(DIR,'logs/info_logs/')
    error_log_path = os.path.join(DIR,'logs/error_logs/')

    #设置日志文件名
    all_log_name = all_log_path + rq + '.log'
    error_log_name = error_log_path + rq + '.log'

    #创建handler
    #创建一个handler，写入所有日志
    fh = logging.FileHandler(all_log_name,encoding="utf-8")
    fh.setLevel(logging.INFO)

    #创建一个handler，写入错误日志
    eh = logging.FileHandler(error_log_name,encoding="utf-8")
    eh.setLevel(logging.ERROR)

    #创建一个handler，输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    #定义日志输出格式
    #以时间-日志器名称-日志级别-日志内容的形式展示
    all_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    # 以时间-日志器名称-日志级别-文件名-函数行号-错误内容
    error_log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s  - %(lineno)s - %(message)s')

    # 将定义好的输出形式添加到handler
    fh.setFormatter(all_log_formatter)
    ch.setFormatter(all_log_formatter)
    eh.setFormatter(error_log_formatter)

    # 给logger添加handler
    logger.addHandler(fh)
    logger.addHandler(eh)
    logger.addHandler(ch)
    return logger


#实例化log，调用时，直接调用log
log = get_log("CL接口自动化")

