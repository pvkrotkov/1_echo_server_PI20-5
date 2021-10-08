import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 9090))
print('Запуск сервера')
sock.listen(0)
print('Начало прослушивания порта')

msg = ''

while True:
	conn, addr = sock.accept()
	print(addr)
	print('Подключение клиента')
	data = conn.recv(1024)

	

	if  data.decode()=='exit':
		print('Отключение клиента')
		break
	msg += data.decode()
	conn.send(data)


	print(msg)

conn.close()

