
def outer():
    a = 1
    def inner():
        nonlocal a
        a = 2
        print(a)
    inner()
    print(a)

outer()


