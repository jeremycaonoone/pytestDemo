# coding=utf-8
# @Time    : 2022/3/17 21:23
# @Author  : 梗小旭
# @File    : public_assert.py
import jsonpath


def assert_res(res, expected_result):
    """
    传入响应体的json格式数据和Excel或yaml中读取的预期结果值，预期结果逐一判断，有一个不符合则返回False
    :param res: 请求返回的响应体数据
    :param expected_result: 预期结果值，例如：'$.code=201;$.success=False;$.message=用户名或密码错误'
    注意：字符串里面不能写引号，比如不能$.message=“用户名或密码错误”，正确写法是：$.message=用户名或密码错误
    :return:
    """
    for exp in expected_result.split(";"):
        rule = exp.split("=")[0]  # jsonpath提取规则
        exp_value = exp.split("=")[1]  # 预期结果值
        reality_value = jsonpath.jsonpath(res, rule)[0]  # 真实返回值
        # 预期结果中存在特殊False和True，读取时要用eval把str类型转成bool，才能和返回值对比判断
        if exp_value == 'False' or exp_value == 'True':
            exp_value = eval(exp_value)
        if str(exp_value) == str(reality_value):
            continue
        else:
            return False
    return True
