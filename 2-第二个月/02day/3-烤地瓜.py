class SweetPotato():

    def __init__(self):
        self.cooklevel = 0 #考的等级
        self.cookstr = "生的"
    def __str__(self):  
        return self.cookstr


    def cook(self,time):
        self.cooklevel+=time
        if self.cooklevel > 0 and self.cooklevel<3:
            self.cookstr = "半生不熟"
        elif self.cooklevel>=3 and self.cooklevel<5:
            self.cookstr = "熟了"
        elif self.cooklevel>=5:
            self.cookstr = "呼了"

sp = SweetPotato()
sp.cook(3)
print(sp)
