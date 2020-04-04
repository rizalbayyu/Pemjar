
def sendalldata (conn, message):
    # Tambahkan termination character di akhir message
    message = message+"\r\n"
    # Kirimkan message
    conn.send(message.encode('ascii'))

def recvalldata(conn):
    data = ""
    # Iterasi untuk membaca data
    while True:
        # Tampung data
        buffer = conn.recv(20)
        buffer = buffer.decode('ascii')
        if "\r\n" in buffer :
            # Bersihkan termchar pada buffer
            buffer = buffer.replace("\r\n", "")
            data = data + buffer
            return data
        else:
            data = data + buffer
        