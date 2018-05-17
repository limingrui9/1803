def test(a):
    def test1(c):
        print(a+c)
    return test1
f = test(1)
f(5)
