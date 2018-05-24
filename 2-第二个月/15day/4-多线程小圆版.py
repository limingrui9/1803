import threading
import time
def sing():
    while True:
        time.sleep(1)
        print("唱歌")

def dance():
    while True:
        time.sleep(1)
        print("跳舞")

t = threading.Thread(target = sing)
t1 = threading.Thread(target = dance)

t.start()
t1.start()
