import socket
from time import sleep
#создаем объект сокета
sock = socket.socket()
sock.setblocking(1) #задаем блокирующий параметр
print("Соединение с сервером")
sock.connect(('localhost', 9090)) #подсоединяемся к порту 9090 локального хоста
print("Соединено с сервером")
while True: #отправлдяем сообщения пока не exit
    msg = input("Сообщение серверу: ") #получаем сообщение от пользователя
    # msg = "Hi!"
    print("Отправка данных серверу")
    sock.send(msg.encode()) #кодируем в байты и отправляем сообщение серверу
    if msg == "exit": #если оно было exit то прерываем цикл
        break
    print("Прием данных от сервера")
    data = sock.recv(1024) #получаем сообщение от сервера
    print(data.decode()) #печатаем полученное

print("Разрыв соединения с сервером")
sock.close() #закрываем сокет