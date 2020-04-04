import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Fungsi connect() digunkan client untuk mengirim fungsi SYN pada server

s.connect(("127.0.0.1", 8900))


try:
    i = 0
    while True:

        if i % 2 == 0:
            data = input("Masukkan Input: ")
            s.send( data.encode('ascii') )
            continuedatarcv = s.recv(100)
        else:
            datarcv = s.recv(100)
            datarcv2 = datarcv.decode('ascii')
            print(datarcv2)
        i += 1
except KeyboardInterrupt:
    print()
    print("Client is death")