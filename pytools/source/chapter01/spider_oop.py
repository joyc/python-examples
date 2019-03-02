from lxml import html
from typing import NamedTuple

import requests


class BootEntity(NamedTuple):
    """ 书本信息 """
    title: str
    price: float
    link: str
    store: str

    def __str__(self):
        return '价格: {self.price} ；名称：{self.title} ; 购买链接：{self.link} 店铺：{self.store}'.format(self=self)


class MySpider(object):

    def __init__(self, sn):
        self.sn = sn
        # 存储所有的书本信息
        self.book_list = []

    def dangdang(self):
        """ 爬取当当网的数据 """
        """ 爬取当当网的数据 """
        url = 'http://search.dangdang.com/?key={sn}&act=input'.format(sn=self.sn)
        # 获取html内容
        html_data = requests.get(url).text

        # xpath对象
        selector = html.fromstring(html_data)

        # 找到书本列表
        ul_list = selector.xpath('//div[@id="search_nature_rg"]/ul/li')
        print(len(ul_list))
        for li in ul_list:
            # 标题
            title = li.xpath('a/@title')
            print(title[0])
            # 购买链接
            link = li.xpath('a/@href')
            print(link[0])
            # 价格
            price = li.xpath('p[@class="price"]/span[@class="search_now_price"]/text()')
            print(price[0].replace('¥', ''))

            # 商家
            store = li.xpath('p[@class="search_shangjia"]/a/text()')
            store = '当当自营' if len(store) == 0 else store[0]
            print(store)
            print('-----------------------')

            book = BootEntity(
                title=title[0],
                price=price[0].replace('¥', ''),
                link=link[0],
                store=store[0]
            )
            print(book)
            self.book_list.append(book)

    def jd(self):
        """ 爬取京东的数据 """
        return []

    def taobao(self):
        """ 爬取淘宝的数据 """
        return []

    def yhd(self):
        """ 爬取一号店的数据 """
        return []

    def spider(self):
        """ 得到排序后的数据 """
        self.dangdang()
        self.jd()
        print('--------------------------------')
        bk_list = sorted(self.book_list, key=lambda item: float(item.price), reverse=True)
        for book in bk_list:
            print(book)

if __name__ == '__main__':
    client = MySpider('9787115428028')
    client.spider()