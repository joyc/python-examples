from lxml import html


def parse():
    """ 将html文件中的内容，使用xpath进行提取 """
    # 读取文件中的内容
    f = open('./static/index.html', 'r', encoding='utf-8')
    s = f.read()

    selector = html.fromstring(s)
    # 解析H3标题
    h3 = selector.xpath('/html/body/h3/text()')
    print(h3[0])


    # 解析ul下面的内容
    # ul = selector.xpath('/html/body/ul/li')
    ul = selector.xpath('//ul/li')
    print(len(ul))
    for li in ul:
        print(li.xpath('text()')[0])

    # 解析ul指定的元素值
    ul2 = selector.xpath('/html/body/ul/li[@class="important"]/text()')
    print(ul2)

    # 解析a标签的内容
    a = selector.xpath('//div[@id="container"]/a/text()')
    # 标签内的内容
    print(a[0])
    # href属性
    alink = selector.xpath('//div[@id="container"]/a/@href')
    print(alink[0])

    # 解析P标签
    p = selector.xpath('/html/body/p[last()]/text()')
    print(len(p))
    print(p[0])

    test = selector.xpath('/html/body/ul/li[3]/text()')
    print(test[0])

    f.close()



if __name__ == '__main__':
    parse()