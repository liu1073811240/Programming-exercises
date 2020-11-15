
name = '全局变量'
def change_name():
    name = '局部变量'
    print('change_name', name)

change_name()
print(name)