import requests
from bs4 import BeautifulSoup

# 需求：爬取诗词名句网站中三国演义小说的所有章节标题和章节内容 https://www.shicimingju.com/book/sanguoyanyi.html


# 对首页进行爬取
url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
headers = {
   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
r = requests.get(url,headers=headers)
r.encoding = r.apparent_encoding
page_text = r.text

# 1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
soup = BeautifulSoup(page_text,'lxml')
li_list = soup.select('.book-mulu > ul >li ')
fp = open('./sanguo.txt','w',encoding='utf-8')
for i in li_list:
    title = i.a.string
    detail_url = 'https://www.shicimingju.com' + i.a['href']
    detail_page_text = requests.get(url=detail_url,headers=headers)
    detail_page_text.encoding = detail_page_text.apparent_encoding
    detail_page_text=detail_page_text.text
    detail_soup = BeautifulSoup(detail_page_text,'lxml')
    content =detail_soup.find('div',class_='chapter_content').text
    fp.write(title + ':' + content + '\n')
    print(title + ':' + '爬取完成！')

fp.close()
