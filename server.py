import socket

sock=socket.socket() 
sock.bind(('', 9090)) 
sock.listen(0) 
conn, addr=sock.accept() 
while True:
    data=conn.recv(1024) 
    if not data: 
        conn, addr=sock.accept() 
        continue
    print(data)
    conn.send(data.upper()) 
