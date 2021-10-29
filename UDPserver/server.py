import random
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
portt = 12345
max = 65355

def working():
    while True:
        try:
            sock.bind(('127.0.0.1', portt))
            print(f'Working on {portt}...\n')
            break
        except OSError:
            port = random.randint(1024, 65355)

    activeClients = []
    while True:
        msg, addr = sock.recvfrom(max)
        print(f'Client{addr}: {msg.decode("ascii")}')
        if not msg:
            continue

        if addr not in activeClients:
            activeClients.append(addr)
        msg = f'Client{addr[1]}: {msg.decode("ascii")}'
        for client in activeClients:
            if client == addr:
                continue
            sock.sendto(msg.encode(), client)

if __name__ == '__main__':
    working()






# def authentication(conn, addr):
#     global clients
#     with open('clients.txt', 'a+') as clients:
#         for client in clients:
#             if str(addr) in clients:
#                 print(f'Hello {clients[1]}!')
#         else:
#             sock.send('Hello, please sign up'.encode())
#             sock.send('Write your login'.encode())
#             data1 = sock.recv(1024)
#             sock.send('So, write your password')
#             data2 = sock.recv(1024)
#             clients.write(str(addr)+': '+data1.decode()+' '+data2.decode())
#             sock.send('Welcome!')

