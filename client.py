import socket

sock = socket.socket()
sock.setblocking(1)
sock.connect(('127.0.0.1', 9090))
print('Соединение с сервером')
msg = input()

sock.send(msg.encode())
print('Отправка данных серверу')
data = sock.recv(1024)
print('Прием данных')
sock.close()

print(data.decode())
