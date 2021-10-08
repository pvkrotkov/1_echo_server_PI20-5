import socket
sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

sock.sendto("check".encode(), ("127.0.0.1", 9090)) 
if sock.recv(1024).decode() == "False":
    name = input("Введите ваш ник: ")
    sock.sendto(name.encode(), ("127.0.0.1", 9090)) 
while True:
    msg = input("text: ")
    if msg == "exit":
        break
    sock.sendto(msg.encode(), ("127.0.0.1", 9090)) 
    print(sock.recv(1024).decode())
sock.close() 
