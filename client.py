import socket
import threading

#функция через которую будем слушать сервер
def listening(sock):
     while True:
         data, server = sock.recvfrom(1024) #получаем сообщение
         print(data.decode()) #выводим на экран


username = input("Введите имя: ") #получаем имя пользователя для чата
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Создаем UDP сокет
sock.sendto((f"Привет, я {username}").encode(), ('localhost', 9090)) #отправляем приветственное сообщение
threading.Thread(target = listening, args = (sock, )).start() # создаем поток прослушивания сообщений от сервера
print('Переписка начата!')
while True: #бесконечно получаем сообщения и отправляем в чат
    message = input()
    sock.sendto((username+": "+message).encode(), ('localhost', 9090)) #отправляем сообщение