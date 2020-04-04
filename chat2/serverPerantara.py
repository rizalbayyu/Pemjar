import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9100))
s.listen(10)
list_conn = []

#Fungsi unuk eksekusi setiap thread
def handle_thread(conn):
    try:

        while True:
            data = conn.recv(100)
            data = data.decode('ascii')
            print("Berhasil terima dari Pengirim")
            for i in list_conn:
                i.sendall(data.encode('ascii'))
    except (socket.error, KeyboardInterrupt):
        conn.close()
        print("Disconnected from client")
try:

    while True:
        conn, cln_address = s.accept()
        list_conn.append(conn)
        print(f"Connection from {cln_address} has been established")
    #Buat thread baru setiap ada koneksi baru
        clientThread=threading.Thread(target=handle_thread, args=(conn,))
        clientThread.start()
except KeyboardInterrupt:
    print()
    print("Server is death")