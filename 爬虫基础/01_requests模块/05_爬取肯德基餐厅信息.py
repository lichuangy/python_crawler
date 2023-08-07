import requests

path = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

keyword = input('please input keyword:')

param = {
    'cname':'',
    'pid':'',
    'keyword':keyword,
    'pageIndex': '1',
    'pageSize': '10',
}

headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

response = requests.post(url=path,params=param,headers=headers)

# print(type(response))
# <class 'requests.models.Response'>
# 这表示response变量是一个requests.models.Response类的实例。
# 通过响应对象,我们可以访问诸如状态码、响应头、响应体等信息:
# print(response.status_code)
# print(response.headers['Content-Type'])
# print(response.text)

content = response.text
print(content)

with open(keyword + '.txt','w',encoding='utf-8') as f:
    f.write(content)
print('保存成功！！！')