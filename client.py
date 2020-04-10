import socket
import sys
import struct

text = "Hello World"
num = 1

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    print("Input text:")
    text = sys.stdin.readline().strip()
    ss = struct.pack("!50si",text.encode(),num)
    s.sendto(ss,("127.0.0.1",1998))
    if text == "bye":
        break
