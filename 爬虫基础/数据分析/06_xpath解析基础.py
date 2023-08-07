# 从lxml模块中导入etree,用于解析和遍历XML/HTML文档
from lxml import etree

if __name__ == '__main__':

    #实例化一个etree对象，且将被解析的本地源码文件加载到了该对象中
    tree = etree.parse('./郭公辅挽诗原文_龚诩_古诗词网.html')
    # ’/‘表示从根节点开始定位，表示一个层级，逐步的定位到body下的所有直系的div
    # r = tree.xpath('/html/body/div')

    # // 表示多个层级，可以从任意位置开始定位
    # r = tree.xpath('/html//div')

    # 属性定位，例如根据div的class来定位
    # r = tree.xpath('//div[@class="gushici"]')

    # 根据索引定位，例如div下面直系所有a标签下：a[1] （索引从1开始）
    # r = tree.xpath('//div[@class = "shici-pic-box"]/div/a[1]')

    # 获取文本，通过 /text() 获取直系下的文本  或者 //text() 获取所有的的文本
    # r = tree.xpath('//div[@class = "shici-pic-box"]/div/a[1]/text()')

    # 获取属性： /@attrName 例如 img src href
    # 获取属性:/@attrName,例如获取img标签的src属性:
    # img_src = tree.xpath('//img/@src')
    r = tree.xpath('//div[@class = "shici-pic-box"]/div/a[1]/@href')
    print(r)
    # 打印获取到的href属性值