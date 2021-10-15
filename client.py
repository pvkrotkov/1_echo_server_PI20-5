import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:

    print('Введите сообщение')
    msg = input()
    client.sendto(msg.encode('utf-8'), ('127.0.0.1', 9090))

    msgfromserver = client.recv(1024).decode("utf-8")
    print('Получение ответа от сервера')

    if msgfromserver=='выход':
        break
        
    print('Ответ сервера: ', msgfromserver)

client.close()



