from btsocket import *

HOST = ""
PORT = 6969

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

fortune = u""
while True:
    data = s.recv(1024)
    if not data:
        break
    fortune += data
    
s.close()

from appuifw import note
note(fortune, "info")
