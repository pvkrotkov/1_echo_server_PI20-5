import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9090))

while True:
    line = input()
    sock.send(line.encode())
    try:
        data = sock.recv(1024)
    except:
        break
    print(data.decode())
sock.close()
