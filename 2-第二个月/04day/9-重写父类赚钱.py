class Father():

    def makemoney(self):
        print("双手赚钱")

class Son(Father):

    def makemoney(self):
        print("用脑子赚钱")
        super().makemoney()

lmr = Son()
lmr.makemoney()
