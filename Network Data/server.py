import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 7501))
s.listen(5)

while True:
    conn, cln_address = s.accept()
    print(f"Connection from {cln_address} has been established")
    data = conn.recv(8)
    data = struct.unpack("<ii", data)
    jumlah = data[0] + data[1]
    jumlah1 = struct.pack("<i", jumlah)
    conn.send(jumlah1)
    print("Berhasil Terima data dan mengirim balik")
