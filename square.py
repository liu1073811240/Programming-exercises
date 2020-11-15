# 定义函数，输出5*5的正方形
# 函数不使用就不执行

def pr_tr():
    for i in range(5):
        for j in range(5):
            print("* ", end="")
        print()

    print()


for i in range(3):
    pr_tr()

