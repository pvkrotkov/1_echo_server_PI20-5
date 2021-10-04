#server
import socket #подключаем библиотеку

sock = socket.socket() #создаём сокет
sock.bind(('localhost',9090)) #прописываем соединение с нужным портом
sock.listen() # <слушаем> порт
conn, adr = sock.accept() #принимаем подключение с помощью метода accept, который возвращает кортеж с двумя элементами - сокет, адрес клиента
answer='' #для формирования ответа
print('Server are up')#обёртка
print(adr)#обёртка
while True:
    data=conn.recv(1024) #принимаем ответ
    if not data:
        print('connection lost')
        break
    answer+=data.decode()#декодируем ответ
    edited_answer=answer.encode() #кодируем ответ
    conn.send(edited_answer)#посылаем ответ
    print(answer)
    answer=''
conn.close() #закрываем соединение.
