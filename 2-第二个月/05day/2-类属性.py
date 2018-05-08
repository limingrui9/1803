class Dog():
    count = 1#类属性
    def __init__(self,name):
        self.name = name
        Dog.count +=1
    def wark(self):
        print("汪汪叫")#实例方法
    @classmethod
    def test(cls):
        print("这是类方法")

    @classmethod
    def change(cls):
        cls.count +=1
        #Dog.count +=1

taidi = Dog("泰迪")
print(taidi.name)
taidi.wark()
Dog.test()
Dog.change()
print(Dog.count)
print(taidi.count)
