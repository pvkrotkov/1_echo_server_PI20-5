import socket
print ('запуск')
sock=socket.socket()
sock.bind(('localhost',9090))
print('связываем сокет с хостом и портом')
print('запускаем прослушивание')
sock.listen()
print('подключение клиента к серверу')
conn,addr = sock.accept()
print(addr)
msg=''
print('считываем данные от клиента порциями по кб')
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
