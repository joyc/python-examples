# 以下的代码的输出将是什么? 说出你的答案并解释？
# def extendList(val, list=[]):
#     print('-----------------')
#     print(list, id(list))
#     list.append(val)
#     print(list, id(list))
#     return list
#
# list1 = extendList(10)
# list2 = extendList(123,[])
# list3 = extendList('a')
#
# print("list1 = {0}".format(list1))
# print("list2 = {0}".format(list2))
# print("list3 = {0}".format(list3))
#

# def add(num):
#     print('-------------')
#     print(num, id(num))
#     num += 2
#     print(num, id(id))
#     return  num
#
# n = 100
# print(n, id(n))
# rest = add(n)
# print(rest, id(rest))
# print(n, id(n))


def change(old_list):
    new_list = old_list
    if len(new_list) > 5:
        new_list = ['ok', 'ok']
    new_list[0] = 'no'
    return new_list

data = [1,2,3, 5,6,7]
print(data, id(data))
rest = change(data)
print(rest, id(rest))
print(data, id(data))