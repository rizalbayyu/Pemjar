import socket
from termcharsendrecv import recvalldata, sendalldata

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Fungsi connect() digunkan client untuk mengirim fungsi SYN pada server

s.connect(("127.0.0.1", 7501))

while True:

    #Kirim data
    data = "Infrastructure and software development teams are increasingly building and managing infrastructure using automated tools that have been described as infrastructure as code. The process of managing and provisioning computing infrastructure and their configuration through machine-processable, declarative, definition files, rather than physical hardware configuration or the use of interactive configuration tools."
    sendalldata(s, data)
    data1 = recvalldata(s)
    print(data1)