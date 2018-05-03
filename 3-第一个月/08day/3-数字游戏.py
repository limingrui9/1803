import random
diannao = random.randint(1,100)
for i in range(1,11):

    c = int(input("请输入数字"))
    if diannao > c:
        print("对不起你猜小了")
    elif diannao == c:
        print("哈哈，被你猜中了")
    else :
        print("你又猜大了，不好意思哈")
