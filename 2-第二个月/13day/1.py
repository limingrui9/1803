def w1(fun):
    def inner():
        print("验证")
        fun()
    return inner
@w1
def test():
    print("哈哈")


#f = w1(test)
#f()
#@w1#相当于test = w1(test)
test = w1(test)
test()
