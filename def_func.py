# 定义函数，计算两数之和
# 1.该功能的实现是否需要未知数的参与？
# 2.如果需要，要几个？
# 什么时候定义函数？凡是我们需要描述某个功能的时候，都将它定义为函数。

# def add(a, b):
#     print(a + b)
#
# add(7, 8)
# add(12, 13)
# def my_max(a, b):
#     if a > b:
#         print(a)
#     else:
#         print(b)

List = [4, 1, 8, 9, 2, 5]


def my_sort(my_list, flag):
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            if flag == True:
                if my_list[i] > my_list[j]:
                    temp = my_list[i]
                    my_list[i] = my_list[j]
                    my_list[j] = temp
            else:
                if my_list[i] < my_list[j]:
                    temp = my_list[i]
                    my_list[i] = my_list[j]
                    my_list[j] = temp

    print(my_list)


my_sort(List, True)
my_sort(List, False)
List.sort(reverse=True)
print(List)
