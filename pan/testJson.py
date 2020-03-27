#!/usr/bin/python3

import json

# Python 字典类型转换为 JSON 对象
data1 = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data1)

data3 = ""
json_str2 = json.dumps(data3)
print(json_str2.encode("UTF-8").decode("UTF-8"))
# print("Python 原始数据：", repr(data1))
# print("JSON 对象：", json_str)

# 将 JSON 对象转换为 Python 字典
data2 = json.loads(json_str)
print("data2['name']: ", data2['name'])
print("data2['url']: ", data2['url'])

# print(json_str2)