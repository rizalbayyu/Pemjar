import socket
import select

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("", 8900))

s.listen(10)

#List aktifitas input yang di monitor

list_monitor = [s]
list_conn = []
try:

    while True:
    # cek aktivitas I/O
        inready, outready, errready = select.select(list_monitor, [],[])
    #iterasi semua aktivitas input yang siap dieksekusi
        for i in inready:
        #Aktivitas input berhubungan dengan socket -> fungsi accept()
            if i == s:
            #Terima permintaan koneksi
                conn, client_addr = s.accept()
            #Tambahkan koneksi baru ke list yang di monitor
                list_monitor.append(conn)
                list_conn.append(conn)
        #Aktivitas input berhubungan dengan koneksi -> fungsi recv()
            else:
                try:
                    data = i.recv(100)
                    data = data.decode('ascii')
                    datarcv = data
                    # i.send(datarcv.encode('ascii'))
                    for j in list_conn:
                        j.sendall(datarcv.encode('ascii'))
                except socket.error:
                    list_monitor.remove(i)
                    print("Client disconnected")
except KeyboardInterrupt:
    print()
    print("Server Down!!!")