import socket  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 7501))         
s.listen(5)   

try:
    while True:
        conn, address = s.accept()
        print (f"Got connection from {address}")
        file = open("test_file_1.pdf","wb") # Write on binary mode
        while (True):       
    # receive data and write it to file
            recvdata = conn.recv(4)
            while (recvdata):
                recvdata = conn.recv(4) #Trying to receive data again from client if thereis another data.
                if not recvdata:
                    file.close()
                    break
                else:
                    file.write(recvdata) #write data to test_file_1.pdf

except KeyboardInterrupt:
    s.close()
    print()
    print("Server Down, check file on the directory")
