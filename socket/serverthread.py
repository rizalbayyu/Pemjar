import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9050))
s.listen(10)

#Fungsi unuk eksekusi setiap thread
def handle_thread(conn):
    try:

        while True:
            data = conn.recv(100)
            data = data.decode('ascii')
            data = "OK "+data
            # Kirim balik ke client
            conn.send(data.encode('ascii'))
    except (socket.error, KeyboardInterrupt):
        conn.close()
        print("Disconnected from client")
try:

    while True:
        conn, cln_address = s.accept()
        print(f"Connection from {cln_address} has been established")
    #Buat thread baru setiap ada koneksi baru
        clientThread=threading.Thread(target=handle_thread, args=(conn,))
        clientThread.start()
except KeyboardInterrupt:
    print()
    print("Server is death")