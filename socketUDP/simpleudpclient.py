import socket

#inisiasi objek socket UDP dengan IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Kirim ke server

server_addr = ("127.0.0.1", 9090)
data = "Selamat sore"
s.sendto(data.encode('ascii'), server_addr)

#Terima balasan dari server
data = s.recv(65536)

data.decode('ascii')

print(data)
s.close()