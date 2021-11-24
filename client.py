import socket
import sys

Host = '127.0.0.1'  
Port = 80
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((Host , Port))
print("Connected to : localhost on port: " + str(Port))
print("Type /q to quit")
print("Enter message to send...")

msgin = ""
msgout = ""
while (msgin != "/q"):
    msgout = input(">")
    s.sendall(str.encode(msgout))
    msgin = s.recv(4096)
    msgin = str(msgin, "utf-8")
    print(msgin)

s.close()
