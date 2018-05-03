account = 1234
passwd = 99999
money = 88888

myaccount = int(input("请输入账号"))
mypasswd = int(input("请输入密码"))
if myaccount == account and mypasswd == passwd:
    print("登录成功")
    mymoney = int(input("请输入取得金额"))
    if money>mymoney:
        print("您取了%d元,还剩%d元"%(mymoney,money-mymoney))
    else:
        print("对不起，你的余额不够，还剩%dmoney")



else:
    print("密码错误非法账户")
