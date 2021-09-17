import socket

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	msg = data.decode()
	conn.send(data)
	if (data.decode() == "exit"):
		break
	print(msg)

conn.close()
