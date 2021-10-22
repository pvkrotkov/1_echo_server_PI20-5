import socket 
print ('Создается сокет')
sock=socket.socket()
sock.bind(('localhost',9090))#установили хост и сервер
print('режим прослушивания')
sock.listen()
print('принимаем подключение клиента к серверу')
conn,addr=sock.accept()
print(addr)
msg=''
print('считываем данные от клиента порциями по кб')
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('',9091))
client = [] # Массив где храним адреса клиентов
print ('сервер активен')
while True:
    print('отправка данных клиенту')
    data=conn.recv(1024)
    if not data:
        break
    msg += data.decode()
    conn.send(data)
    print(msg)
    msg=''
print('отключение клиента')
print('остановка сервера')
conn.close()
data ,address = sock.recvfrom(1024)
print (address[0], address[1]) #выводим информацию об ip и хосте
if address not in client :
    client.append(address)
    for clients in client :
        if clients == address :
            continue
            sock.sendto(data,clients)
print('Сервер завершил работу')
