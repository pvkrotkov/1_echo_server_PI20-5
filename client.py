import socket
sock = socket.socket()
print(' соединяем с сервером')
sock.connect(('localhost', 9090))
print('выход осуществляется через команду exit')
while True:
    msg = input()
    if msg == "exit":
        print('разрыв соединения с сервером')
        break
    print('посылаем данные серверу')
    sock.send(msg.encode())
    print('принимаем данные от сервера')
    data = sock.recv(1024)
    print(data.decode())
sock.close()
