import json
from datetime import datetime

import MySQLdb
import requests
from flask import Flask, redirect, request

app = Flask(__name__)

token = {}


def get_conn():
    """ 获取mysql 的连接 """
    try:
        conn = MySQLdb.connect(
            db='db_user',
            host='localhost',
            user='root',
            password='',
            charset='utf8'
        )
    except:
        pass
    return conn


def get_ticket():
    url = 'https://api.weibo.com/oauth2/authorize?client_id=3428987103&response_type=code&redirect_uri=http://test.baidu.com'
    # get请求
    return url


def get_token(code):
    '''
    获取token
    :param code:
    :return:
    '''
    url = 'https://api.weibo.com/oauth2/access_token?client_id=3428987103&client_secret=0b4aa2dba36b9191015feed2e45e8f1b&grant_type=authorization_code&redirect_uri=http://test.baidu.com&code=' + code
    resp = requests.post(url)
    global token
    token = resp.json()
    return token


def get_info(access_token, uid):
    url = 'https://api.weibo.com/2/users/show.json'
    resp = requests.get(url, {
        'access_token': access_token,
        'uid': uid
    })
    return resp.json()


def weibo_share(access_token):
    '''
    分享数据到微博
    :param access_token:
    :return:
    '''
    url = 'https://api.weibo.com/2/statuses/share.json'
    resp = requests.post(url, {
        'access_token': access_token,
        'status': '现在是北京时间： {0} http://test.baidu.com'.format(datetime.now())
    })
    return resp.json()


@app.route('/')
def index():
    code = request.args.get('code', None)
    # 根据code来获取token
    token = get_token(code)
    # 获取用户信息

    user_info = get_info(token['access_token'], token['uid'])
    third_id = user_info['id']
    nickname = user_info['screen_name']
    headimg = user_info['profile_image_url']

    # 获取数据库的链接
    conn = get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO `user`(`third_id`, `nickname`, `headimg`) VALUES('{third_id}', '{nickname}', '{headimg}')".format(
        third_id=third_id, nickname=nickname, headimg=headimg)
    print(sql)
    cursor.execute(sql)
    conn.autocommit(True)
    return json.dumps(user_info)


@app.route('/weibo')
def weibo():
    ticket = get_ticket()
    return redirect(ticket)


@app.route('/share')
def share():
    global token
    print(token)
    rest = weibo_share(token['access_token'])
    return json.dumps(rest)


if __name__ == '__main__':
    app.run(debug=True, port=80)