#!/usr/bin/env python
"""
chtml.py: Replacing img urls for html file.
__author__ = "chaung.li"
"""
from re import compile
from shutil import copyfile
from json import load


def backup(filename):
    file_name = filename + '.bak'
    copyfile(filename, file_name)
    print(f'{file_name} Backup done!')


def dic():
    with open('images.json', 'r') as load_f:
        j_dict = load(load_f)
    return j_dict


def get_html():
    read_data = ''
    with open('index.html', 'r+', encoding='utf-8') as f:
        read_data = f.read()
    return read_data


def replace():
    with open('index_ok.html', 'w', encoding='utf-8') as f:
        html = get_html()
        j_dic = dic()
        num = len(j_dic)
        for (k, v) in j_dic.items():
            regex = compile('<img src=\"(.*{})'.format(k))
            url = regex.search(html).group(1)
            html = html.replace(url, v)
        f.write(html)
        print(f'{num} images have been replaced done')


if __name__ == '__main__':
    backup('index.html')
    replace()
