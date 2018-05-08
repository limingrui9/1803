class Person():
    def sleep(self):
        print("睡觉")

    def eat(self):
        print("吃吃")

    def study(self):
        print("学习")
    def introduce(self):
        print("身高%d体重%d"%(self.height,self.weight))

yangzhenya = Person()

yangzhenya.sleep()
yangzhenya.eat()
yangzhenya.study()

yangzhenya.height = 180
yangzhenya.weight = 80
yangzhenya.introduce()
