import socket
import struct
import sys
import binascii

def crc32(v):
     r = binascii.crc32(v.encode())
     return r


"""if len(sys.argv) != 3:
    print("Useage: python " + sys.argv[0] + " <ip> <liseten port>")
    sys.exit(-1)"""

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    print("Input text:")
    text = sys.stdin.readline().strip()
    ss = struct.pack("!50sL",text.encode(),crc32(text))
    s.sendto(ss,("127.0.0.1",1998)) #send to forwarder
    s.sendto(ss,("127.0.0.1",1999))
    if text == "bye":
        break
