import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((socket.gethostname(), 4096))

while True:
    data,addr = s.recvfrom(1024)
    data.decode('ascii')
    print(data)
    print(addr)
