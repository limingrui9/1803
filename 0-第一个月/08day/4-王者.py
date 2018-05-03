s_account = "lmr"
s_passwd = "123465"
count = 1

while True:
    account = str(input("请输入账号"))
    passwd = str(input("请输入密码"))
    if account == s_account and passwd == s_passwd:
        hero = input("0-ADC 1-肉 2-法师 3-刺客")
        if hero == 0:
            print("鲁班")
        elif hero == 1:
            print("程咬金")
        elif hero == 2:
            print("王昭君")
        elif hero == 3:
            print("至尊宝")
        break
    else:
        print("错误了%d次"%count)
        count +=1
        if count == 4:
            print("账号异常")
            break
