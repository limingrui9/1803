person = ["lmr","laowang","haha"]
for i in person:
    print("我邀请%s共进晚餐"%i)

print("%s来不了"%person[0])
person[0] = "haha"
for i in person:
    print("我邀请%s共进晚餐"%i)

