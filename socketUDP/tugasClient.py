import socket

#inisiasi objek socket UDP dengan IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ("127.0.0.1", 9090)
data = "100, 200, +"
s.sendto(data.encode('ascii'), server_addr)