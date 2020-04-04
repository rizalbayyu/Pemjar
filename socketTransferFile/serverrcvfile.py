import socket  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("127.0.0.1", 7501))         
s.listen(5)   

try:

    while True:
        conn, address = s.accept()
        print (f"Got connection from {address}")
        i=1
        file = open('test_file_'+ str(i)+".pdf",'wb')
        i=i+1
        while (True):       
    # receive data and write it to file
            recvdata = conn.recv(1024)
            while (recvdata):
                file.write(recvdata)
                recvdata = conn.recv(1024)
        file.close()
        conn.close()
except KeyboardInterrupt:
    print("Server Down, check file on the directory")
    s.close()