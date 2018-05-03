

print("*****这是一个神奇的计算器*****")


a = float(input("请输入一个心仪数字"))
b = float(input("请输入一个数字"))
fuhao = input("请输入+-×/")

if fuhao == "+":
    print(a+b)

elif fuhao == "-":
    print(a-b)
elif fuhao == "×":
    print(a*b)
elif fuhao == "/":
    print(a/b)
