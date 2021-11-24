import socket
import sys

Host = '127.0.0.1'  
Port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Host, Port))
s.listen()
print("Server listening on: localhost on port: " + str(Port))
print('Connected by (' + Host + ', ' + str(Port) + ')')
print("Waiting for message...")

client_connection, client_address = s.accept()


msgin = ""
msgout = ""
msgin = client_connection.recv(4096)
msgin = str(msgin, "utf-8")
print(msgin)
print("Type /q to quit")
print("Enter message to send...")
msgout = input(">")
client_connection.sendall(str.encode(msgout))

while (msgout != "/q"):
    msgin = client_connection.recv(4096)
    msgin = str(msgin, "utf-8")
    print(msgin)
    msgout = input(">")
    client_connection.sendall(str.encode(msgout))
client_connection.close()   
s.close()