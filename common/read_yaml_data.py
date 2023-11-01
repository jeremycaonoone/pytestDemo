# coding=utf-8
# @Time    : 2022/3/16 14:58
# @Author  : 梗小旭
# @File    : read_yaml_data.py
import os

import yaml
from common.public_path import DIR
from common.read_file_func import execute_func
from common.get_dict_api import update_dict_val,add_params
class ReadYamlData():

    def __init__(self,filename):
        self.path=os.path.join(DIR,f"data/{filename}.yaml")


    def read_yaml_case(self):
        """
        读取yaml文件中数据并返回
        :return:
        """

        with open(self.path,"r",encoding="utf-8") as f:
            data=f.read()
        result=yaml.load(data,Loader=yaml.FullLoader)

        return result

    def yaml_to_list(self,n=None):
        """
        把读取yaml的数据转成list中多个tuple，每个tuple放url，data,expected_result,参数化使用
        当yaml文件中存在rules规则时，表明该条用例存在接受其他接口传参，读取rules下的规则数据，如下：
        position：想要修改数据字典中的key的路径，例如["department","id"],配置文件中写department.id，通过split分解
        method：需要调用的函数名称
        module：需要调用的函数所在模块及文件路径，例如：interface_data.jiekou，interface_data模块名，jiekou文件名称
        params：调用函数所需要的传参，不需要传参时，默认写[]
        :param n 对应第几条用例，n为None时，返回全部用例
        :return:
        """
        result=self.read_yaml_case()
        all_case_list=[]
        for temp_case in result:
            case_list=[]
            #判断读取的数据中是否存在rules规则
            if "rules" in temp_case:
                data = temp_case['data']
                for rules in temp_case["rules"]:
                    position=rules["position"].split('.')
                    func_name=rules["method"]
                    module_name=rules["module"]
                    params=rules["params"]
                    #读取配置文件中的函数，并执行函数返回值
                    result=execute_func(func_name=func_name, module_name=module_name,params=params)
                    #更新data值
                    update_dict_val(data,position,val=result)
                #把数据加到all_case_list中
                case_list.append(temp_case["url"])
                case_list.append(data)
                case_list.append(temp_case["expected_result"])
                all_case_list.append(tuple(case_list))
            else:
                case_list.append(temp_case["url"])
                case_list.append(temp_case["data"])
                case_list.append(temp_case["expected_result"])
                all_case_list.append(tuple(case_list))
        #判断n的值，为None时，返回所有的值，n为具体数字时，返回某个案例
        if n==None:
            return all_case_list
        else:
            return all_case_list[n-1]
