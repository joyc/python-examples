#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2019/2/16/0017 18:06
# @Author  : Hython.com
# @File    : tk_test.py
# from tkinter import Tk, StringVar
# from tkinter.ttk import Button, Entry, Label
# from tkinter.filedialog import askopenfilename
# from tkinter.messagebox import showinfo

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as msg
from tkinter import Menu


from re import compile
from json import load


class mainWin:

    def __init__(self):
        self.win = tk.Tk()
        # tt.create_tooltip(self.win, 'Hello GUI')
        self.win.title("SMC画像URL置換くん v0.2")
        self.create_widgets()

    def pick_json(self):
        global j_path
        j_path = askopenfilename(title="Select json file", filetypes=(("json files", "*.json"), ("all files", "*.*")))
        global json_path
        json_path.set(j_path)

    def pick_html(self):
        global h_path
        h_path = askopenfilename(title="Select html file", filetypes=(("html files", "*.html"), ("all files", "*.*")))
        global html_path
        html_path.set(h_path)

    def get_dic(self, j_path):
        with open(j_path, 'r') as f:
            j_dict = load(f)
        return j_dict

    def get_html(self, h_path):
        with open(h_path, 'r+', encoding='utf-8') as f:
            html_data = f.read()
        return html_data

    def img_url_rp(self):
        with open('index_ok.html', 'w', encoding='utf-8') as f:
            html = self.get_html(h_path)
            j_dic = self.get_dic(j_path)
            num = len(j_dic)
            for (k, v) in j_dic.items():
                regex = compile('<img src=\"(.*{})'.format(k))
                url = regex.search(html).group(1)
                html = html.replace(url, v)
            f.write(html)
            msg.showinfo('Finish', f'{num} images have been replaced urls done!')

    # quit
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    ##########################################

    def create_widgets(self):
        mighty = ttk.LabelFrame(self.win, text='SMC image url replace settings ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        # add labels
        j_label = ttk.Label(mighty, text="select your json file:")
        j_label.grid(column=0, row=0, columnspan=3, sticky='W')
        h_label = ttk.Label(mighty, text="select your html file:")
        h_label.grid(column=0, row=2, columnspan=3, sticky='W')

        label_j = ttk.Label(mighty, text="json file:")
        label_j.grid(column=0, row=1, sticky='W')
        label_h = ttk.Label(mighty, text="html file:")
        label_h.grid(column=0, row=3, sticky='W')

        # add pading for every label
        for child in mighty.winfo_children():
            child.grid_configure(padx=4)

        # add textbox
        global json_path
        json_path = tk.StringVar()
        j_file_entered = ttk.Entry(mighty, width=35, textvariable=json_path)
        j_file_entered.grid(column=1, row=1, sticky='W')

        global html_path
        html_path = tk.StringVar()
        h_file_entered = ttk.Entry(mighty, width=35, textvariable=html_path)
        h_file_entered.grid(column=1, row=3, sticky='W')

        # add button
        self.btn1 = ttk.Button(mighty, text='select', command=self.pick_json).grid(row=1, column=2)
        self.btn2 = ttk.Button(mighty, text='select', command=self.pick_html).grid(row=3, column=2)

        self.button = ttk.Button(mighty, text="Replace", command=self.img_url_rp)
        self.button.grid_configure(pady=8)
        self.button.grid(column=1, row=5)

        # add menu
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        # add menu name
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # showinfo
        def _msgBox():
            msg.showinfo('Version：', 'SMC画像URL置換くん v0.2:\n\nMA_Tools\nBy Li @2019')

        # second menu
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.win.iconbitmap('link.ico')


mainWin = mainWin()
mainWin.win.mainloop()