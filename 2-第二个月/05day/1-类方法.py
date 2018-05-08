class Dog():
    def __init__(self,name):
        self.name = name
    def wark(self):
        print("汪汪叫")#实例方法

    @classmethod
    def test(cls):
        print("这是类方法")

taidi = Dog("泰迪")
print(taidi.name)
taidi.wark()
Dog.test()
taidi.test()

