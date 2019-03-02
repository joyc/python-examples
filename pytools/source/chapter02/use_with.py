

def open_file():
    """ 使用with语法打开一个文件 """
    try:
        f = open('./static/test.txt', 'r', encoding='utf-8')
        rest = f.read()
        print(rest)
    except:
        pass
    finally:
        f.close()


    # with open('./static/test.txt', 'r', encoding='utf-8') as f:
    #     rest = f.read()
    #     print(rest)


if __name__ == '__main__':
    open_file()