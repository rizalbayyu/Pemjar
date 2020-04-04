import socket

#inisiasi objek socket UDP dengan IPv4
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#Bind server agar bisa menerima data dari semua IP dengan port 9090
s.bind(("0.0.0.0", 9090))

while True:
# Terima data dari client

#Fungsi recv() return data yang diterima 1, yaitu data yang dikirim
#Fungsi recvfrom() return data yang diterima 2, yaitu data dan address sender
#Fungsi receive bersifat blocking
    data, client_addr = s.recvfrom(65536)

# convert array of bytes to string

    data = data.decode('ascii')
    print(data)
# Tambah "OK" di depan data

    data = "OK " +data

#Kirim balik ke client
    s.sendto(data.encode('ascii'), client_addr)

#Tutup socket
s.close()
