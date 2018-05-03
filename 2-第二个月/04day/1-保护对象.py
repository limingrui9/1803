class Dog():

    def __init__(self,age):
        self.__age = age

    def wark(self):
        print("汪汪叫")

    def getAge(self):
        return self.__age
   
    def __str__(self):
        return("狗的年龄是%d"%self.__age)
hsq = Dog(10)
print(hsq.getAge())
print(hsq)
hsq.wark()


