class Cat():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sleep(self):
        print("猫在睡觉")
    def cat(self):
        print("猫在吃鱼")

tom = Cat()
tom.sleep()
tom.eat()
print(id(tom))

bosimao = Cat()
bosimao.sleep()
bosimao.eat()
