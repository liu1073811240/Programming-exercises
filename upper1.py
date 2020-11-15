# a = [1, 2]
# def change(c):
#     c.append(3)
#     return c
#
# change(a)
# print(a)
# print(change(a))

# string是不可变的，凡是对string做操作，都在重新创建一个新的string。
a = 'abc'
def change(c):
    g = c.upper()
    return g

print(change(a))
print(a)



