class Person():
    def __init__(self,money):
        self.__money = 100
    def getMoney(self):
        return self.__money
    def setMoney(self,money):
        if money <= 0:
            print("传入金额非法")
        else:
            self.money = money

xiaoming = Person(10)
#xiaoming.__money = -100
xiaoming.setMoney(20)
print(xiaoming.getMoney())

