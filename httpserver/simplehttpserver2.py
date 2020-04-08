import socket
import os
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 9100))
s.listen(10)
list_conn = []

#Fungsi unuk eksekusi setiap thread
def handle_thread(conn):
    try:
        # Baca Header
        headers = ""
        while True:
            temp = conn.recv(4)
            temp = temp.decode('ascii')
            headers = headers + temp
            if "\r\n\r\n" in headers:
                headers.replace("\r\n\r\n", "")
                break
        #Cetak headers yang diterima
        headersSplit = headers.split('/')
        request = headersSplit[1]
        request = request.replace(" HTTP", "")
        if "HTTP" in headers:

            print(headers)
            file = open("index.html", "r")
            filesize = os.stat("index.html").st_size
            filesize = str(filesize)
            #Kembalikan response ke client
            response = ("HTTP/1.1 200 OK\r\n" + 
                        "Content-Type: text/html\r\n" + 
                        "Content-Length: "+ filesize +"\r\n" + 
                        "Connection: close\r\n" + 
                        "\r\n" + 
                        file.read())
            print(response)
            conn.send(response.encode('ascii'))
            file.close()
    except (socket.error, KeyboardInterrupt):
        conn.close()
        print("Disconnected")
try:

    while True:
        conn, cln_address = s.accept()
    #Buat thread baru setiap ada koneksi baru
        clientThread=threading.Thread(target=handle_thread, args=(conn,))
        clientThread.start()
except KeyboardInterrupt:
    print()
    print("Server is death")