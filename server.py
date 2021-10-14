import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind (('',9090))
cli_list = [] #Адерса клиентов для пересылки
print ('Запуск сервера')
while True:
        data ,addr = sock.recvfrom(1024) #получаем сообщение от клиента
        
        if addr not in cli_list : #проверяем есть ли такой клиент
                cli_list.append(addr) #добавляем клиента если такого еще нет
        for cli in cli_list: #отправляем сообщения клиентам
                if cli != addr: #если отправитель не он сам же
                	sock.sendto(data,cli) #то отправляем сообщение клиента

