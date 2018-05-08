class Game():
    
    def __init__(self):
        self.__size = 100

    def getSize(self):
        return self.__size

    def setSize(self,size):
        self.__size = size

    def __dazhao(self,mp):
        print("十步杀一人")

    def fadazhao(self,mp):
        if mp <= 80:
            print("蓝不够")
        else:
            self.__dazhao(mp)

wangzhe = Game()
wangzhe.fadazhao(100)
a = wangzhe.getSize()
print(a)
#print(wangzhe.__size)
