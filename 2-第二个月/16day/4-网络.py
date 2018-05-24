from socket import *

#创建udp
s = socket(AF_INET,SOCK_DGRAM)

s.sendto("哈哈".encode("gb2312"),("192.168.1.2",8080))


s.close()
