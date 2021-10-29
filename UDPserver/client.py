import socket, threading, os

max = 65355
sock = socket.socket

def listen(sock):
    while True:
        msg = sock.recv(max)
        print('\r\r' + msg.decode('ascii') + '\n' + f'You >>> ', end='')

def connect():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        port = int(input('Write the port to connect >>> '))
        try:
            sock.connect(('127.0.0.1', port))
            print('Connected')
        except:
            print('Port is close... Retry please')
            continue

        threading.Thread(target=listen, args=(sock,), daemon=True).start()

        sock.send('Join in the chat'.encode('ascii'))

        while True:
            msg = input('You >>> ')
            sock.send(msg.encode('ascii'))



if __name__ == '__main__':
    os.system('clear')
    connect()

