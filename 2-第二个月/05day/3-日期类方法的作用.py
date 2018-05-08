class DateTest():
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    def outDate(self):#实例方法
        print("%s年%s月%s日"%(self.year,self.month,self.day))
    @classmethod
    def handleDate(cls,date):
        a,b,c = date.split("-")
        #cls(a,b,c)相当于DateTest(a,b,c)
        #d = DateTest(a,b,c)

        d =cls(a,b,c)#初始化实例对象

        return d

#第一种
a = 2018
b = 05
c = 04
d = DateTest(a,b,c)
d.outDate()

#我就给你传一个2018-05-04
#第一步:先处理字符串
#第二步:实例化对象
str = "2018-05-06"
a,b,c = str.split("-")

d = DateTest(a,b,c)
d.outDate()

#通过类方法
str = "2019-06-07"
#a,b,c = DateTest.handleDate(str)
#d = DateTest(a,b,c)
#d.outDate()

#优化
d = DateTest.handleDate(str)
d.outDate

#DateTest.hadlerDate(str).outDate()

