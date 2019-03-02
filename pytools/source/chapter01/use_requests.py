import requests

def get_book(sn):
    """ 获取书本的信息 """
    url = 'http://search.dangdang.com/'
    rest = requests.get(url, params={
        'key': sn,
        'act': 'input'
    })
    print(rest.text)
    # json的方式获取数据
    # rest.json()
    print(rest.status_code)
    print(rest.encoding)
    rest.encoding = 'utf-8'


    # HTTP状态码
    # 2x
    # 4x 404 403
    # 500


    # requests.post()

if __name__ == '__main__':
    get_book()