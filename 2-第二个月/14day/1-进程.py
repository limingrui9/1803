import os
import time

ret = os.fork()

if ret ==  0:
    print("我是子进程%d pid=%d ppid=%d"%(ret,os.getpid(),os.getppid()))

else:
    print("我是父进程%d pid=%d ppid=%d"%(ret,os.getpid(),os.getppid()))
