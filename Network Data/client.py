import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Fungsi connect() digunkan client untuk mengirim fungsi SYN pada server

s.connect(("127.0.0.1", 7501))

while True:

    #Kirim data
    #Definisikan 2 angka integer signed

    a = 200
    b = 100
    data = struct.pack("<ii", a, b)
    s.send(data)
    data1 = s.recv(4)
    data2 = struct.unpack("<i", data1)
    print(data2[0])