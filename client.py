#client
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket #подключаем библиотеку

UDP_MAX_SIZE=65535

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #создаём сокет
sock.connect(('localhost', 8083)) #прописываем соединение с нужным портом
while True: #бесконечный цикл
    message=input('Enter your message here') #отправка сообщений на сервер
    if message=='exit': #проверка на exit - при получении вырубает циел
        print('Connection with server was lost') #обёртка
        break
    encoded=message.encode() #перевод сообщения в байт-код
    sock.send(encoded) #посылаем сообщение на сервер

    data = sock.recvfrom(UDP_MAX_SIZE) #получаем ответ от сервера
    print(data.decode()) #переводим сообщение из байт-кода

sock.close() #закрываем соединение.
