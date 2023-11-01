# coding=utf-8
from typing import Dict, List


def get_dict(dict_value, obj_key, default=None):
    """
    遍历字典，得到想要的value
    :param dict_value: 所需要遍历的字典
    :param obj_key: 所需要value的键
    :param default:进行取值中报错时所返回的默认值 (default: None)
    :return:
    """
    for k, v in dict_value.items():
        if k == obj_key:
            return v
        else:
            if type(v) is dict:  # 如果键对应的值还是字典
                re = get_dict(v, obj_key, default)  # 递归
                if re is not default:
                    return re


def get_list_dict(list_value, obj_key, obj_value):
    """
    遍历列表中的每个字典，判断obj_key,obj_value值是否存在，存在则任何True，否则False
    :param list_value: 所需要遍历的列表
    :param obj_key: 想要判断的key
    :param obj_value: 想要判断的value
    :return:
    """
    for dict_value in list_value:
        for k, v in dict_value.items():
            if k == obj_key and v == obj_value:
                return True
            else:
                continue
    # 列表中所有数据都不存在时，返回False
    return False


def updata_dict_value(dict_data, obj_key, update_value=None):
    """
    遍历字典，得到想要的key对象，给读取文件时修改值,如果obj_key存在一样的情况下，就会改错
    :param dict_value: 所需要遍历的字典
    :param obj_key: 所需要value的键
    :return:
    """
    for k, v in dict_data.items():
        if k == obj_key:
            dict_data[k] = update_value
        else:
            if type(v) is dict:  # 如果键对应的值还是字典
                updata_dict_value(v, obj_key, update_value)  # 递归


def update_dict_val(data: Dict, key_list: List, val: int, i=0):
    """
    传入data字典格式数据，根据对应的key_list,把对应的key的val值修改
    :param data: 传入的字典数据
    :param key_list: 传入修改的key list，例如["department","id"],配置文件中写department.id，通过split分解
    :param val: 想要修改的值
    :param i: i值默认为0，递归时默认+1
    :return:
    """
    if i == len(key_list) - 1:
        data[key_list[i]] = val
        return
    return update_dict_val(data[key_list[i]], key_list, val, i=i + 1)


def add_params(func_str, params):
    """
    根据传入的函数名称，和函数所需要的数据来拼接成函数传参的字符串格式，通过eval转成可以执行的函数
    :param func_str: 函数的名称，必须传字符串
    :param params: 函数所需要的参数，params是一个list，例如函数为：add(a，b,c=4),huanc
    :return:
    """
    value = ",".join([str(i) for i in params])
    val = f'{func_str}({value})'

    return eval(val)
