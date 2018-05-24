import threading
import time
def saySorry():
    print("亲爱的，我头你妈")
    time.sleep(1)

if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=saySorry)
        t.start()

