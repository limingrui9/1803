class Pig():
    def sleep(self):
        print("哼哼哼")
    def eat(self):
        print("猪饲料")

    def introduce(self):
        print("我叫%s年龄%d颜色%s"%(self.name,self.age,self.color))


peiqi = Pig()
peiqi.age = 12
peiqi.name = "小猪佩琪"
peiqi.color = "粉色"
peiqi.eat()
peiqi.sleep()
peiqi.introduce()

qz = Pig()
qz.age = 10
qz.name = "乔治"
qz.color = "蓝色"
qz.eat()
qz.sleep()
qz.introduce()
