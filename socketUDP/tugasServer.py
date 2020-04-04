import socket
import re
import operator

#inisiasi objek socket UDP dengan IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 9090))

data, client_addr = s.recvfrom(65536)

# convert array of bytes to string

data = data.decode('ascii')
arr = re.split(',', data)
ang1 = int(arr[0])
ang2 = int(arr[1])
op = str(arr[2])
if op == " +":

    hitung = ang1 + ang2
    print(hitung)

s.close()