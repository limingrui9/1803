def w1(fun):
    def inner(*args,**kwargs):
        print("___-验证——————")
        ret = fun(*args,**kwargs)
        return ret
    return inner

@w1
def test(a,b):

    print("a==%d b==%d"%(a,b))
    return"hehehehe"

@w1
def test1():
    print("哈哈哈")

@w1
def test2(a,b):
    print("呵呵呵")

@w1
def test3():
    return"嘎嘎嘎"

test1()
test2(1,2)
print(test3())
print(test(1,2))
