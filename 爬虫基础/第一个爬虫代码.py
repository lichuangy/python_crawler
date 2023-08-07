# 需求：第一个爬虫程序，爬取自己博客页面

# 1. 导入requests模块
import requests

def requests_test():
    # 2. 指定url地址
    path = 'https://www.sog ou.com/'
    # 3. 发起请求
    content = requests.get(url=path)
    # 4. 获取响应数据
    response = content.text
    print(response)
    # 5. 存储数据结果
    with open('./sogo.html','w',encoding='utf-8') as f:
        f.write(response)
    print('保存结束')
if __name__ == '__main__':
    requests_test()
