#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/2/16/0017 18:06
# @Author  : Hython.com
# @File    : tk_test.py
from tkinter import Tk, StringVar
from tkinter.ttk import Button, Entry, Label
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo

from re import compile
from json import load


j_path = ''
h_path = ''


def pick_json():
    global j_path
    j_path = askopenfilename()
    json_path.set(j_path)


def pick_html():
    global h_path
    h_path = askopenfilename()
    html_path.set(h_path)


def dic(j_path):
    with open(j_path, 'r') as load_f:
        j_dict = load(load_f)
    return j_dict


def get_html(h_path):
    read_data = ''
    with open(h_path, 'r+', encoding='utf-8') as f:
        read_data = f.read()
    return read_data


def replace_code():
    with open('index_ok.html', 'w', encoding='utf-8') as f:
        html = get_html(h_path)
        j_dic = dic(j_path)
        num = len(j_dic)
        for (k, v) in j_dic.items():
            regex = compile('<img src=\"(.*{})'.format(k))
            url = regex.search(html).group(1)
            html = html.replace(url, v)
        f.write(html)
        showinfo('Finish', f'{num} images have been replaced done!')


win = Tk()
win.title('画像URL置換くん v0.1')
win.geometry('435x80')
win.resizable(0, 0)

json_path = StringVar()
html_path = StringVar()
label1 = Label(win, text="json file:").grid(row=0, column=0)
Entry(win, textvariable=json_path, width=50).grid(row=0, column=1)
btn1 = Button(win, text='select json', command=pick_json).grid(row=0, column=2)

label2 = Label(win, text="html file:").grid(row=1, column=0)
Entry(win, textvariable=html_path, width=50).grid(row=1, column=1)
btn2 = Button(win, text='select html', command=pick_html).grid(row=1, column=2)
btn3 = Button(win, text='replace', command=replace_code).grid(row=2, column=1)

win.mainloop()
