import socket
import sys
import struct
import random
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 1998))
while True:
    data, addr= s.recvfrom(1024)
    str,num = struct.unpack("!50sL",data)
    str = str.decode("utf-8").replace("\0","")
    r = random.randint(1,10)
    if str == "bye":
        break
    if r <= 4:
        str = "different"
    ss = struct.pack("!50sL",str.encode(),num)
    s.sendto(ss,("127.0.0.1",1999))
    print("sending {} and {} to server".format(str,num))

