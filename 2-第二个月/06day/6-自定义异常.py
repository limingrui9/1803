class ShowError(Exception):
    def __init__(self,len,leastlen):
        self.len = len
        self.leastlen = leastlen

def main():
    #抛出一个小于3位的异常
    try:
        s = input("请输入")
        if len(s)<3:
            raise ShowError(len(s),3)
    except ShowError as ret:
        print("你传的位是%d，至少需要%d位"%(ret.len,ret.leastlen))
main()
