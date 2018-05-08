class Pig():
    def sleep(self):
        print("哼哼哼")

    def eat(self):
        print("猪饲料")

    def introduce(self):
        print("我叫%s年龄%d颜色%s"%(peiqi.name,peiqi.age,peiqi.color))
peiqi = Pig()
peiqi.age = 12
peiqi.color = "粉色"
peiqi.name = "小猪佩琪"
peiqi.eat()
peiqi.sleep()
peiqi.introduce()
