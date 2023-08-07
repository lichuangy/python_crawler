"""
User-Agent的作用和意义:
1. 标识客户端信息
User-Agent字符串包含使用的浏览器名称、版本、操作系统等信息,服务器端可以解析该字符串来识别客户端信息。
2. 调整内容展示
网站可以根据User-Agent提供不同的网页版本,以适应移动端或者不同浏览器的展示效果。
3. 统计分析
可以通过分析User-Agent统计不同用户使用的客户端信息,做出客群分析。
4. 辨别爬虫行为
网站可以检测可疑的User-Agent来发现爬虫程序。

为什么要进行User-Agent伪装:
1. 伪装浏览器避免被识破
有些网站会阻止没有浏览器身份标识的请求,所以需要伪装成浏览器的User-Agent。
2. 访问仅针对特定客户端的资源
一些网站会对搜索爬虫和移动用户提供不同版本的页面,需要通过User-Agent来获取。
3. 防止被识别为爬虫而被封禁
一些网站会检测可疑的爬虫User-Agent并做封禁,伪装可以避免被检测。
4. 统计分析不准确
使用真实的User-Agent会使网站统计到错误的用户信息,伪装可以避免这种情况。
综上,User-Agent伪装可以帮助程序以浏览器的身份访问网站,获得更好的适配效果,也有助于隐藏程序行为避免被检测。


"""


# 导包
import requests

# path = 'https://www.sogou.com/web?query=是小李同学&'
path = 'https://www.sogou.com/web'

# 动态输入参数
kw = input("please input you query word:")
# 处理url携带的参数，封装到字典中
params = {'query':kw}
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
# 对指定的url发起请求对应的url是携带参数的，并且请求过程中处理了参数，UA伪装
response = requests.get(url=path,params=params,headers=headers)
content = response.text
print(content)

# 结果存储
filename = kw + '.html'
with open(filename,'w',encoding='utf-8') as f:
    f.write(content)
print(filename,'保存成功！')