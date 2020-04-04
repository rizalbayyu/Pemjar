import socket
# import sys        

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
s.connect(("127.0.0.1", 7501))

filename = "test1.pdf"
file = open(filename, "rb")
readfile = file.read(1024)
while (readfile):
    s.send(readfile)
    readfile = file.read(1024)
s.close()