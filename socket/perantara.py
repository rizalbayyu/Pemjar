import socket

#Inisiasi socket TCP/IPv4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind
s.bind(("127.0.0.1", 2502))
#Listen sebanyak jumlah backlog
s.listen(5)
while True:

    #Fungsi accept() digunakan oleh server untuk mengirim fungsi SYN-ACK ke client

    conn, cln_address = s.accept()
    print(f"Connection from {cln_address} has been established")
    
    # Receive dari client
    data = conn.recv(100)
    data = data.decode('ascii')
    print("Berhasil terima data dari client")
    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s1.connect(("127.0.0.1", 7501))
    data = "OK "+data
    s1.send(data.encode('ascii'))