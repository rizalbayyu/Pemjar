import struct

def sendalldata(conn, message):
    # Hitung ukuran data
    datasize = len(message)
    datasize = struct.pack("<I", datasize)
    #Kirim data
    message = message.encode('ascii')
    # Tambahkan ukuran message pada konten
    data = datasize+message
    #Kirim data
    conn.send(data)

def recvalldata(conn):
    #Baca ukuran data
    datasize = conn.recv(4)

    # Unpack untuk membaca ukuran message
    datasize = struct.unpack("<I", datasize)[0]

    # Pembacaan Message
    message = conn.recv(datasize)
    message = message.decode('ascii')
    return message