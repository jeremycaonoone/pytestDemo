# coding=utf-8
# @Time    : 2022/3/10 15:52
# @Author  : 梗小旭
# @File    : base_method_api.py

from common.log import log
import requests
import traceback
from common.config_operate_api import Config


class BaseMethodApi():

    def __init__(self):
        self.conf = Config().getconf("enviro")
        self.host = self.conf.host
        self.url = self.conf.url
        self.data = self.conf.data

    def get_token_data(self):
        """
        获取当前环境下的token值
        :return: 返回登录成功的token值
        """
        complete_ulr = "http://" + self.host + self.url  # 完整url
        res = requests.post(url=complete_ulr, json=eval(self.data), headers=self.choice_headers())
        token = res.json()['data']['token']['access_token']
        return token

    def choice_headers(self, type=None):
        """
        封装选择请求头信息，type等于None时，请求头不传token，等于其他值时传token
        :param type:
        :return:
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            "Content-Type": "application/json; charset=utf-8"
        }
        if type:
            headers["Authorization"] = self.get_token_data()
            return headers
        else:
            return headers

    def get(self, url, params=None, headers=None, files=None):
        """
        get请求
        :param url: 请求路径
        :param params: 请求参数
        :param headers: 请求头
        :param files: 请求文件
        :return:
        """
        try:
            log.info("============请求信息============")
            complete_ulr = "http://" + self.host + url  # 完整url
            if not headers:
                headers = self.choice_headers(type=1)
            else:
                headers = self.choice_headers()
            res = requests.get(url=complete_ulr, params=params, headers=headers, files=files)
            log.info(f"请求url：{complete_ulr}")
            log.info(f"请求参数:{params}")
            log.info(f"请求头:{headers}")
            log.info("============响应信息============")
            log.info(f"响应状态码：{res.status_code}")
            log.info(f"响应结果：{res.text}")
            return res
        except:
            log.error("============请求失败信息============")
            log.error(f"请求异常：{traceback.print_exc()}")

    def post(self, url, data=None, json_data=None, headers=None, files=None):
        """
        post请求
        :param url: 请求路径
        :param data: 原始请求参数
        :param json_data: json格式请求参数
        :param headers: 请求头
        :param files: 请求文件
        :return:
        """
        try:
            log.info("============请求信息============")
            complete_ulr = "http://" + self.host + url  # 完整url
            if not headers:
                headers = self.choice_headers(type=1)
            else:
                headers = self.choice_headers()
            res = requests.post(url=complete_ulr, data=data, json=json_data, headers=headers, files=files)
            log.info(f"请求url：{complete_ulr}")
            if json_data == None:
                log.info(f"请求参数:{data}")
            else:
                log.info(f"请求参数:{json_data}")
            log.info(f"请求头:{headers}")
            log.info("============响应信息============")
            log.info(f"响应状态码：{res.status_code}")
            log.info(f"响应结果：{res.text}")
            return res
        except:
            log.error("============请求失败信息============")
            log.error(f"请求异常：{traceback.print_exc()}")
