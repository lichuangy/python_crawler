python
# 导入请求模块
import requests
# 导入json模块用来处理json数据
import json

# 豆瓣电影Top250接口URL
path = 'https://movie.douban.com/j/chart/top_list'

# 参数,可根据实际情况调整
param = {
    'type': '24', # 电影类型,24代表榜单类型为Top250
    'interval_id': '100:90',
    'action':'',
    'start': '0', # 开始位置,从0开始
    'limit': '20',# 获取条数
}

# 请求头,修改UA伪装浏览器
headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

# 发送GET请求
response = requests.get(url=path,params=param,headers=headers)

# 获取响应内容并解析成json格式
content = response.json()

# 打印结果
print(content)

# 打开文件准备写入
fp = open('douban.json', 'w', encoding='utf-8')

# 将content的数据转换成字符串写入
fp.write(str(content))

print('finish!')