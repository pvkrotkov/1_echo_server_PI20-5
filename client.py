import socket
from time import sleep

sock = socket.socket()
sock.setblocking(1)
print("Соединение с сервером")
sock.connect(('localhost', 9090))
print("Соединено с сервером")
while True:
    msg = input("Сообщение серверу: ")
    # msg = "Hi!"
    print("Отправка данных серверу")
    sock.send(msg.encode())
    if msg == "exit":
        break
    print("Прием данных от сервера")
    data = sock.recv(1024)
    print(data.decode())

print("Разрыв соединения с сервером")
sock.close()