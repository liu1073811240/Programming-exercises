
def HaveFun():
    if __name__ == '__main__':
        print("我在执行自己，我的名字是： %s" % __name__)
    else:
        print("y有人调用我！，我的名字是： %s" % __name__)

HaveFun()
print(dir())  # 返回当前模块所有变量的名称

print(__name__)




