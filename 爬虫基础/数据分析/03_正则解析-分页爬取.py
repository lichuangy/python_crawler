import requests
import re
import os

# 导入需要的模块

# <dd>主人,你就可怜可怜我吧!!<br><img src="https://pic.biedoul.com/Uploads/Images/34/595e2100b2af2.jpg"><br></dd>
# 需求:爬取别逗网站中图片模块下的所有图片
if __name__ == '__main__':

    # 判断作为主程序运行

    # 创建存放图片目录
    if not os.path.exists('./biedou/pic'):
        os.makedirs('./biedou/pic')

    # 检查目录是否存在,不存在则创建目录

    # 爬取地址
    url = 'https://www.biedoul.com/pic/'

    # 定义要爬取的网址

    # 代理UA
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    # 设置请求头信息
    for page_num in range(1,3):
        new_url = url + str(page_num)
        page_text = requests.get(new_url, headers=headers).text

        # 使用requests获取网页内容

        # 使用聚焦爬虫将页面中的所有图片进行解析/提取
        ex = re.compile(r'<DD>.*?<br><img src="(.*?)"/><br></DD>', re.S)
        image_list = re.findall(ex, page_text)

        # 使用正则表达式提取图片链接

        for i in image_list:
            image_data = requests.get(i, headers=headers).content
            with open('./biedou/pic/' + str(page_num) + '_' + i.split('/')[-1], 'wb') as f:
                f.write(image_data)
    # 遍历图片链接,请求图片内容并保存文件