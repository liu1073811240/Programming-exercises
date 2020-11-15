total = 0

def sum(arg1, arg2):
    global total
    total = arg1 + arg2# 想让局部的total和全局的total变为同一个total(通过里面的操作，改变外面的值）
    print("局部变量", total)
    return total

sum(1, 2)
print("全局变量", total)