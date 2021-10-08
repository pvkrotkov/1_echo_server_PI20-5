import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.bind(('127.0.0.1', 9090)) 

clients = {}
while True:
    data, addr=sock.recvfrom(1024) 
    if data.decode() == "check":
        if addr in clients:
            sock.sendto("True".encode(), addr)
        else:
            sock.sendto("False".encode(), addr)
        continue
    if addr not in clients:
        clients.update({addr : data.decode()})
        continue
    for client in clients:
        sock.sendto((clients[addr] + ": %s" % data.decode()).encode(), client)
