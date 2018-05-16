def w1(fun):
    def inner():
        print("————验证————")
    return inner

@w1
def test():
    print("哈哈哈")
    return "hehehe"


print(test())
