class Girl():
    #用初始化对象的一些属性
    def __init__(self,age,height):
        self.age = age
        self.height = height
        self.address = "河南"
        self.games = []

    def study(self):
        print("学习")

    def opencar(self,car):
        print("一定会开车%s"%car)

    def showage(self):
        print("年龄%d"%self.age)

    def addgames(self,game):
        self.games.append(game)

    def showgames(self):
        for i in self.games:
            print(i)



louxueman = Girl(12,170)
louxueman.study()
louxueman.opencar("宝马")
louxueman.showage()
#加游戏
louxueman.addgames("王者")
louxueman.showgames()
print(id(louxueman))

xiaoyuan  = Girl(16,180)
xiaoyuan.study()
xiaoyuan.opencar("拖拉机")
xiaoyuan.addgames("最强谈谈")
xiaoyuan.showgames()
print(id(xiaoyuan))

