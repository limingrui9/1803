class Person():
    def __init__(self):
        self.money = 100

wxx = Person()
wxx.money = -100
print(wxx.money)
