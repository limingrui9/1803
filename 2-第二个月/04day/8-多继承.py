class A():
    def testA(self):
        print("-----A------")

    def test(self):
        print("-----testA----")

class B():
    def testB(self):
        print("----------B--------")

    def test(self):
        print("----------testB-------")
#当A B类里面有相同的方法的时候，调用方法的顺序就是继承的顺序
class C(A,B):
    pass

c =C()

c.testA()
c.testB()
c.test()
print(C.__mro__)
