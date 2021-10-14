#server
import socket #подключаем библиотеку

#UDP_MAX_SIZE=65535

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #создаём сокет
sock.bind(('localhost', 8083)) #прописываем соединение с нужным портом

answer='' #для формирования ответа
print('Server are up')#обёртка
while True:
    print(sock.recv(65535)) #для удобства тестирования
    data, addr=sock.recv(1024) #принимаем ответ
    if not data:
        print('connection lost')
        break
    answer+=data.decode()#декодируем ответ
    sock.sendto(answer.encode('utf-8'), addr)##кодируем ответ u посылаем ответ
    print(answer)
    answer=''
conn.close() #закрываем соединение.
