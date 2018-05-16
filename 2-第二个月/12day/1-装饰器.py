def w1(fun):
    def inner():
        print("验证")
        fun()
    return inner

@w1
def test():
    print("哈哈哈")

@w1
def test1():
    print("haha")

f = w1(test)
f()



f1 = w1(test1)
f1()
