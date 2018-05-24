import os
import time

rpid = os.fork()

num = 0#time.sleep(5)

while True:
    os.fork()


if rpid == 0:
    num += 1
    time.sleep(5)

    print("我是父进程")
    print("我是父进程%d"%num)
else:
    time.sleep(2)
    num -= 1
    print("我是子进程")
    print("我是子进程%d"%num)
print("我是大王")
