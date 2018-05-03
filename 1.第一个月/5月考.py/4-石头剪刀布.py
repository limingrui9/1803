#1=石头
#2=剪刀
#3=步

'''
import random
while True:
    computer = random.randint(1,3)
    me = int(input("请输入1-石头 2-剪刀 3-步"))
    if (computer==1 and me==2) or (computer==2 and me==3) or (computer==3 and me==1):
        print("电脑赢了")
    elif computer == me:
        print("平局")
    else:
        print("我赢了")
'''

def youxi():
    import random
    while True:
        computer = random.randint(1,3)
        me = int(input("请输入1-石头 2- 剪刀 3-步"))
        if (computer==1 and me==2) or (computer==2 and me==3) or (computer==3 and me==1):
            print("电脑赢")
        elif computer == me:
            print("平局")
        else :
            print("玩家赢")

youxi()
