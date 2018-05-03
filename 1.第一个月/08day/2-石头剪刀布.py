'''
1:石头
2:剪刀
3:布
'''
import random

while True:
    computer = random.randint(1,3)
    player = int(input("请输入1:石头 2:剪刀 3:布"))
    if player <=3 and player>0:
        if(player==1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer ==1):
            print("你赢了")
        if(player == computer):
            print("平局")
        else:
            print("你赢了")
    else:
        print("输入不合法")


