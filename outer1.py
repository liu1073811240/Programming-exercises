
name = "张三"  # 内建变量
def outer():
    a = 3 #闭包
    def inner():
        b = 2  # 局部
        print(a)
        print(name)

    inner()

outer()
