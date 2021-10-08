import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('',9091))
client = [] # Массив где храним адреса клиентов
print ('server online!')
while True:
         data ,address = sock.recvfrom(1024)
         print (address[0], address[1]) #выводим информацию об ip и хосте
         if address not in client :
                 client.append(address)
         for clients in client :
                 if clients == address :
                     continue
                 sock.sendto(data,clients)
print('Server is shutting down')
