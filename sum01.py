
def add(a, *b):
    sum = 0
    for i in b:
        sum += i
    return a + sum

print(add(1, 3, 5, 8))






