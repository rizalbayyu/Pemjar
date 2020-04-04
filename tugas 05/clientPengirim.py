import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Fungsi connect() digunkan client untuk mengirim fungsi SYN pada server

s.connect(("127.0.0.1", 9100))

try:

    while True:
        data = input("Masukkan Input: ")
        s.send( data.encode('ascii') )
except KeyboardInterrupt:
    print()
    print("Client is death")