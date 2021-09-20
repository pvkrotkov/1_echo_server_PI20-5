import socket
def listening():
    sock = socket.socket()
    sock.bind(('', 9090))
    sock.listen(0)
    conn, addr = sock.accept()
    print('connection established ', addr)
    ret=False
    msg = ''

    while True:
        data = conn.recv(1024)
        msg = data.decode()
        print(msg)
        if msg == 'exit':
            ret=True
            break
        if not data:
            break
        conn.send(data)
    print('connetion lost ', addr)
    conn.close()
    return ret
ret = False
while not ret:
    ret = listening()
