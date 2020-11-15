# 打印1-10（不包括8）的整数
a = 0
while a <= 10:

    if a == 8:
        a += 1
        continue
    print(a)
    a += 1

print("程序结束")

