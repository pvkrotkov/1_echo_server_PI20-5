@@ -3,14 +3,13 @@

 sock = socket.socket()
 sock.setblocking(1)
 sock.connect(('10.38.165.12', 9090))

 #msg = input()
 msg = "Hi!"
 sock.send(msg.encode())

 data = sock.recv(1024)

 sock.connect(('localhost', 9090))
 while True:
     msg = input()
     sock.send(msg.encode())
     if msg == 'exit':
         break

     data = sock.recv(1024)
     print(data.decode())
 sock.close()

 print(data.decode())
