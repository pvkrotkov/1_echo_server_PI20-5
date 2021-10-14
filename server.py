import socket
print("Запуск сервера")
sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
print("Начало прослушивания порта")
conn, addr = sock.accept()
print(f"Подключение клиента {addr}")


while True:
	print("Прием данных от клиента")
	data = conn.recv(1024)
	if not data:
		print(f"Отключение клиента {addr}")
		break
	msg = data.decode()
	print(msg)
	print("Отправка данных клиенту")
	conn.send(data)
	if msg == "exit":
		print(f"Клиент попросил отключения {addr}")
		break


print("Остановка сервера")

conn.close()