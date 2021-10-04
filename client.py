#client
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket #подключаем библиотеку

sock = socket.socket() #создаём сокет
sock.connect(('localhost', 9090)) #прописываем соединение с нужным портом
while True: #бесконечный цикл
    message=input('Enter your message here') #отправка сообщений на сервер
    if message=='exit': #проверка на exit - при получении вырубает циел
        print('Connection with server was lost') #обёртка
        break
    encoded=message.encode() #перевод сообщения в байт-код
    sock.send(encoded) #посылаем сообщение на сервер

    data = sock.recv(1024) #получаем ответ от сервера
    print(data.decode()) #переводим сообщение из байт-кода

sock.close() #закрываем соединение.
