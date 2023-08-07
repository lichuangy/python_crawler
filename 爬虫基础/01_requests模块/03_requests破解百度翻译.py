"""

"""


# 导包
import requests
import json

# 百度翻译发送的axios请求
path = 'https://fanyi.baidu.com/sug'

# 动态输入参数
kw = input("please input you query word:")
# 处理url携带的参数，封装到字典中
params = {'kw':kw}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
# 对指定的url发起请求对应的url是携带参数的，并且请求过程中处理了参数，UA伪装
response = requests.post(url=path,params=params,headers=headers)
content = response.text
# 将\u编码转换成中文
print(json.loads(content))

# 字典类型
# print(type(json.loads(content)))


# 结果存储
filename = kw + '.html'
with open(filename,'w',encoding='utf-8') as f:
    # 将字典转换成字符串
    f.write(str(json.loads(content)["data"]))
print(filename,'保存成功！')