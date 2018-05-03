class Pig():
    def eat(self):
        print("能吃")
    def sleep(self):
        print("哼哼哼")

    def introduce(self):
        print("我叫%s年龄%s颜色%s"%(self.name,self.age,self.color))

peiqi = Pig()
peiqi.eat()
peiqi.sleep()
peiqi.name = "小猪佩琪"
peiqi.age = "28"
peiqi.color = "骚粉"
peiqi.introduce()




qz = Pig()
qz.eat()
qz.sleep()
qz.name = "乔治"
qz.age = "12"
qz.color = "黑色"
qz.introduce()

