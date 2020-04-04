import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Fungsi connect() digunkan client untuk mengirim fungsi SYN pada server

s.connect(("127.0.0.1", 2502))

while True:

    #Kirim data
    data = input("Masukkan input: ")
    s.send(data.encode('ascii'))