import socket
print("Запуск сервера")
#создаём объект сокета
sock = socket.socket()
#биндим сокет для любых подключений через порт 9090
sock.bind(('', 9090))
#начинаем прослушиваение
sock.listen(0)
print("Начало прослушивания порта")
conn, addr = sock.accept() #получаем подключение от клиента
print(f"Подключение клиента {addr}")


while True: #запускаем бесконечный цикл приема и отправки пока не пустое и не exit
	print("Прием данных от клиента")
	data = conn.recv(1024) #принимаем 1024 байта информации от клиента
	if not data: #если пустая, то останавливаем цикл
		print(f"Отключение клиента {addr}")
		break
	msg = data.decode() #если не пустая преобразовываем из byte в string
	print(msg) #выводим на экран
	print("Отправка данных клиенту")
	conn.send(data) #отправляем обратно клиенту его же сообщение
	if msg == "exit": #если оно было exit то прерываем цикл
		print(f"Клиент попросил отключения {addr}")
		break


print("Остановка сервера")

conn.close() #закрываем соединение