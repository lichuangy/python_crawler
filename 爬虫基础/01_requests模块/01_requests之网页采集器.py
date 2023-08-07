# 导包
import requests

# path = 'https://www.sogou.com/web?query=是小李同学&'
path = 'https://www.sogou.com/web'

# 动态输入参数
kw = input("please input you query word:")
# 处理url携带的参数，封装到字典中
params = {'query':kw}
# 对指定的url发起请求对应的url是携带参数的，并且请求过程中处理了参数
response = requests.get(url=path,params=kw)
content = response.text
print(content)

# 结果存储
filename = kw + '.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(content)