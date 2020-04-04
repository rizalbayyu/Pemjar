import socket       

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)           
s.connect(("127.0.0.1", 7501))

filename = "test.pdf"
file = open(filename, "rb") #Read on binary mode
readfile = file.read(4) #Put data on file into readfile variable
while (readfile):
    s.send(readfile) #Send data
    readfile = file.read(4) #Read data again on the file
print("Berhasil kirim data")
s.close()
