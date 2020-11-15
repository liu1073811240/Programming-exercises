# 函数把重复的功能封装成模块

a = 2
b = 6
print(a+b)

a = 7
b = 8
print(a+b)

# 1.都在定义变量（变量名，个数一样），都在赋值（值不一样）
# 2.都在输出，求两数之和

# 上面的代码在重复的定义求和，以后如果发现代码中出现了这样的重复性，
# 那么我们一定要将重复的部分进行提取，封装成一个单独的部分，以此来提高代码的复用性。
# python中是通过函数来解决这样的问题的。

def func(a, b):
    return a+b

a = func(3, 5)
print(a)