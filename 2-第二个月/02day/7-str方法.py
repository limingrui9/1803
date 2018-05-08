class Cat():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "名字是%s年龄是%d"%(self.name,self.age)

    def sleep(self,bed):
        print("%s正在%s睡觉"%(self.name,bed))

    def eat(self):
        print("%s猫在吃鱼"%self.name)

tom = Cat("汤姆",40)
tom.sleep("席梦思")
tom.eat()
print(id(tom))
print(tom)
bsm = Cat("博士帽",30)
bsm.sleep("地板")
bsm.eat()
print(id(bsm))
print(bsm)
