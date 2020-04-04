import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 7501))
s.listen(5)

while True:
    conn, cln_address = s.accept()
    print(f"Connection from {cln_address} has been established")
    data = conn.recv(100)
    data = data.decode('ascii')
    print(data)
    print("Berhasil Terima data dari perantara")
