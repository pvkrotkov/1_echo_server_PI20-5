import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('127.0.0.1', 9090))
print('Запуск сервера')

while True:

	data, addr = sock.recvfrom(1024)
	print('Получение ответа от клиента')
	msgfromclient=data.decode('utf-8')

	if msgfromclient=='выход':
		break
		
	print('Ответ клиента: ', msgfromclient)

	reply = input('Введите сообщение ')
	sock.sendto(reply.encode('utf-8'), addr)

sock.close()	



