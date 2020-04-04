import socket
from termcharsendrecv import recvalldata, sendalldata

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 7501))
s.listen(5)

while True:
    conn, cln_address = s.accept()
    print(f"Connection from {cln_address} has been established")
    data = recvalldata(conn)
    data = "OK " +data
    sendalldata(conn, data)
    print("Berhasil Terima data dan mengirim balik")
