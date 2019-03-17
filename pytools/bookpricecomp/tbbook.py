#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/3/16/0016 18:44
# @Author  : Hython.com
# @File    : tb_book.py
# 淘宝更新规则需要先登录才能得到搜索页数据
import requests
import re
if __name__ == '__main__':

    # 设定爬取100页，实际上还要多...
    pages = 2
    for num in range(1, pages + 1):

        print('开始爬取第' + str(num) + '页内容...' + '\n' + '.' * 10)
        url = 'https://s.taobao.com/api?_ksTS=1523191565870_226&callback=jsonp227&ajax=true&m=customized&stats_click=search_radio_all:1&q=macbookpro&p4ppushleft=1,48&ntoffset=4&s=36&imgfile=&initiative_id=staobaoz_20180408&bcoffset=' + str(num) + '&js=1&ie=utf8&rn=5bd3f39c2ca57f21abe4db8ca60ee49f'
        # 代理信息
        header = {
                'cookie': 'v=0; cookie2=1bd112426e98c8a04bca73b7a107c942; _tb_token_=e55f6a754e7db; cna=U2k+E/GqsTECAWqoVXhaddbn; thw=jp; hng=JP%7Czh-CN%7CJPY%7C392; miid=8055327651330014368; publishItemObj=Ng%3D%3D; tracknick=%5Cu521B%5Cu4E16%5Cu754C; dnk=%5Cu521B%5Cu4E16%5Cu754C; tg=0; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; tk_trace=oTRxOWSBNwn9dPyorMJE%2FoPdY8zZPEr%2FCrvCMS%2BFZCFf1lyAe7CQGAWszmcVwVb1HBDBYGRkFkQdtJSeonXvzC0LfgvM0zAV7%2BheyCkpxPv3KHjxWjzAX%2FtU7oCwVLX7zaXJTjAAf%2Fw0sNc6sQY4ZpEkGGlsAFceL7l0gs%2FDembuUGsdJiD4LFB68%2Bno7PV%2FTESKLjU%2B0jCC2sdVyFtfUaYSqLYV0AQRDQjIT3VAO4nz4V6oe6BzeibZQ%2FDX37t50XobzMeTa0cexS4gJxCU%2BNHg7vti3aqS2ng%2Fw0Iv%2BnJcIlhHrjD3IHtUZFA13SZK4zOFGuaq58IDG%2FGwsqDJlHYfJJR8OLRAwIhalk1evatJbiv6zAekE6wtG7maEmjVxBSFYuki5oabAQfP5GuQ3Jw7tLIY477q9jxpxDXB%2F7RK%2FJRa4n4Tt4WB8GJQEOIFVQfOKx9b58k2i3FsWV3OAxUrJGaK85yDKr2MfDghNi%2BJieWQCRz0405RAIaR27XsD9s3NSa%2BFIRpv5WUyMywP9vqJX7Gg32%2BcF9rR1lWUAohIJaiwCByRKKSkdxjHmMEPGP1oiWs2fr2LddX8yJa50%2BAe%2FdeE%2BYaQbekVN%2Bx63iSQYQ%2FcYPSxr9cvdZFEN0mEOkpYQGXVANkf6DmeGg%3D; t=0d4004c898352942830f2312c10f82a1; _fbp=fb.1.1551533224730.690307184; skt=c26d5914f02df3aa; csg=5163aa95; uc3=vt3=F8dByEv1QqPACBm3ZzA%3D&id2=UU6jWcojLco%3D&nk2=13gashZc&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTU1MTUzMzI1MQ%3D%3D; lgc=%5Cu521B%5Cu4E16%5Cu754C; _cc_=U%2BGCWk%2F7og%3D%3D; enc=%2BPvr0AwXBOpmsgdqaSik%2F%2BotG3aUbTbeQtUurEffnJWev4hGw2VdItyemXjMEQfFJL%2BO4px37bk%2F%2BZXmu93%2Fpw%3D%3D; swfstore=228145; whl=-1%260%260%261551533436587; alitrackid=world.taobao.com; mt=ci=-1_0; lastalitrackid=www.jianshu.com; JSESSIONID=A63617B7B6F1FEAB67469F98A3C0908A; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=UIHiLt3xSixwG45%2Bs3wzsA%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&existShop=false&pas=0&cookie14=UoTZ5iITg2Quxw%3D%3D&cart_m=0&tag=8&lng=zh_CN; isg=BKurfm98c37pb6kRdguQvBHoOs9VaL0cAHm6mB0o_upBvMsepZRAkgLVFqR3nBc6; l=bBrk1SL4vaxpTsXJBOCg5uI8UqbTMIRAguPRwdXei_5Qq6T_U8bOl6Fp4F96VA5R_KLB47K_Qsw9-eto9',
                'referer': 'https://s.taobao.com/search?q=macbookpro&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180408&ie=utf8&bcoffset=4&p4ppushleft=1%2C48&ntoffset=4&s=0',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3724.8 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest'}

        responed = requests.get(url=url, headers=header)
        # 指定编码格式
        responed.encoding = 'utf-8'

        re_text = responed.text
        '''
            进入数据清洗与筛选阶段
            因为转化json格式始终失败...所以改用正则表达式来进行匹配
        '''
        print('获取源代码成功，以下为相关商品的信息：')
        target = re.findall(r'"raw_title":"(.*?)".*?"pic_url":"(.*?)".*?"view_price":"(.*?)".*?"item_loc":"(.*?)".*?"view_sales":"(.*?)".*?"user_id":"(.*?)".*?"nick":"(.*?)"', re_text, re.S)  # @UndefinedVariable
        for each in target:
            product = {
                'shop_title':each[0],  # 店铺主题
                'pic_url':'https:' + each[1],  # 店铺图片地址
                'price':each[2],  # 价格
                'sales_people':each[4],  # 购买人数
                'shop_name':each[6],  # 店铺名称
                'loc':each[3],  # 店铺所在地
                'shop_url':'https://store.taobao.com/shop/view_shop.htm?user_number_id=' + each[5]  # 店铺URL地址
                    }
            print(product)