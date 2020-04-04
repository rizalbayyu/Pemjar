import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
data = "Welcome Stranger"
s.sendto(data.encode('ascii'), ((socket.gethostname())))