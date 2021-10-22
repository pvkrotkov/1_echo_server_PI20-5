import socket
print('Cоздается сокет ')
sock = socket.socket()
print(' Соединяется с сервером ')
sock.connect(('localhost', 9090))
print('Остановка сервера происходит после сообщения выход')
while True:
    msg =input()
    if msg=="выход":
        print('разрыв соединения с сервером')
        break
    print('посылаем данные серверу')
    sock.send(msg.encode())
    print('принимаем данные от сервера')
    data = sock.recv(1024)
    print(data.decode())
sock.close()
import threading
def read_sok():
     while True:
         data = sock.recv(1024)
         print(data.decode('utf-8'))
server = '127.0.0.1', 9091
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('', 0))
sock.sendto(' Connect to server'.encode('utf-8'), server)
stream = threading.Thread(target= read_sok) # вызываем функцию read_sok
stream.start()
while True:
    message = input()
    sock.sendto(message.encode('utf-8'), server) #рассылка другим клиентам
