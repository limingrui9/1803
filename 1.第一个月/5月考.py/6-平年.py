def runnian(year):
            if (year%4==0 and year%100!=0) or (year%400==0):
                print("您输入的是闰年")
            else:
                print("您输入的平年")





year = int(input("请输入年"))
runnian(year)
