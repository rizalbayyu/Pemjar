import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9100))
s.listen(10)

#Fungsi unuk eksekusi setiap thread
def handle_thread(conn):
    try:

        while True:
            data = conn.recv(100)
            data = data.decode('ascii')
            print("Berhasil terima dari Pengirim")
            conn1.send(data.encode('ascii'))
    except (socket.error, KeyboardInterrupt):
        conn.close()
        conn1.close()
        print("Disconnected from client")
try:

    while True:
        conn, cln_address = s.accept()
        conn1, cln_address1 = s.accept()
        print(f"Connection from {cln_address} has been established")
    #Buat thread baru setiap ada koneksi baru
        clientThread=threading.Thread(target=handle_thread, args=(conn,))
        clientThread.start()
        print(threading.active_count())
except KeyboardInterrupt:
    print()
    print("Server is death")