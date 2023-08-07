from bs4 import BeautifulSoup
fp = open('./郭公辅挽诗原文_龚诩_古诗词网.html','r',encoding='utf8')
soup = BeautifulSoup(fp,'lxml')
# print(soup)
# print(soup.a)
# print(soup.find('a'))
# print(soup.find('div', class_='navtop'))
print(soup.find_all('a'))

print(soup.select('.navtop'))

soup.select('')