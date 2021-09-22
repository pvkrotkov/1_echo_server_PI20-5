import socket, threading

def s_sendto(sock, data, address):
    global END_FLAG
    sock.sendto((data+END_FLAG).encode(), address)

def s_recvfrom(sock):
    global END_FLAG
    msg, address = '', None
    while True:
        data, server = sock.recvfrom(1024)
        msg += data.decode()
        if not address:
            address = server
        elif server != address:
            print('SOMETHING WRONG')
            raise
        if END_FLAG in msg:
            msg = msg.replace(END_FLAG, '')
            break
    return msg, address


def data_recieve(sock):
    while True:
        print(sock.s_recvfrom()[0])


def data_send(sock):
    while True:
        msg = input()
        if msg == 'leave':

            return None
        sock.s_sendto(msg, (localIP, local_port))


socket.socket.s_sendto = s_sendto
socket.socket.s_recvfrom = s_recvfrom
END_FLAG = '~~~'
STOP_FLAG = True
localIP= "192.168.1.39"
local_port  = 13131
sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.setblocking(True)
sock.s_sendto('starting whith server', (localIP, local_port))

threading.Thread(target = data_recieve, args = (sock,), daemon = True).start()
data_send(sock)

