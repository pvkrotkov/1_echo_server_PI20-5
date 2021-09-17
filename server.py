import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	decoded = data.decode()
	if decoded == 'exit':
		conn.send('Соединение разорвано'.encode())
		conn.close()
		break
	else:
		msg += data.decode()
		conn.send(data)
