import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    msg = input('Enter a message')
    if msg =='exit':
        print('Break connection with a server')
        break
    sock.send(msg.encode())
    data = sock.recv(1024)
    print(data.decode())
sock.close()
