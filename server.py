import random, socket, sys

orig_stdout = sys.stdout
f = open('server_log.txt', 'w')
sys.stdout = f

sock = socket.socket()
portt = 12345

while True:
    try:
        sock.bind(('', portt))
        print("Connect to {}".format(portt))
        break
    except OSError as err:
        print("Port {} not avaliable".format(portt))
        portt = random.randint(1024, 65355)

sock.listen(0)
print("Working...")

def listening(sock):
    conn, addr = sock.accept()
    print("Client {} connect".format(addr))
    with open("client.txt", "a+") as clients:
        clients.seek(0,0)
        for i in clients:
            if addr[0] in i:
                conn.send("Hello" + i.replace(addr[0], '')).encode()
                break
            else:
                conn.send('Enter your name!'.encode())
                username = conn.recv(1024).decode()
                clients.write('\n' + username + addr[0])

    ret = False
    msg = ""

    while True:
        print("Data from client")
        try:
            data = conn.recv(1024)
        except (ConnectionResetError, ConnectionAbortedError) as err:
            print(err, addr)
            return
        msg = data.decode()
        print(msg)
        if msg == "exit":
            ret = True
            break
        if not data:
            break
        conn.send(data)
        print("Sending data to client...")
    conn.close()
    print("Client {} passed out".format(addr))
    return ret

ret = False
while not ret:
    ret = listening(sock)
print("Stop server")

sys.stdout = orig_stdout
f.close()