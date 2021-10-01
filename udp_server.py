import socket, random

def s_sendto(sock, data, address, sender = None, server = False):
    global END_FLAG, ip_username
    if server:
        data = f'~Server:$ {data}{END_FLAG}'
    else:
        data = f"~{ip_username[sender]}:$ {data}{END_FLAG}"
    sock.sendto(data.encode(), address)


def s_recvfrom(sock):
    global END_FLAG
    msg, address = '', None
    while True:
        data, client = sock.recvfrom(1024)
        msg += data.decode()
        if not address:
            address = client
        elif client != address:
            print('SOMETHING WRONG')
            raise
        if END_FLAG in msg:
            msg = msg.replace(END_FLAG, '')
            break
    return msg, address


def listening(sock):
    global ip_username
    while True:
        msg, client = sock.s_recvfrom()
        if client not in ip_username.keys():
            sock.s_sendto('Create your chat name: ', client, server = True)
            ip_username[client] = None
            print(f'Added {client}')
        elif not ip_username[client]:
            if msg not in ip_username.values():
                ip_username[client] = msg
                sock.s_sendto('You are logged on!', client, server = True)
                print(f'{client} got name: {msg}')
            else:
                sock.s_sendto('This name is already used. Create another name!', client, server = True)
        else:
            print(f'from {ip_username[client]}:$ {msg}')
            recipients = list(ip_username.keys())
            recipients.remove(client)
            sock.setblocking(False)
            for address in recipients:
                sock.s_sendto(msg, address, client)
                try:
                    sock.s_recvfrom()
                except BlockingIOError:
                    pass
                except ConnectionResetError as err:
                    print(ip_username.pop(address), address, err)
            sock.setblocking(True)


socket.socket.s_sendto = s_sendto
socket.socket.s_recvfrom = s_recvfrom
END_FLAG = '~~~'
ip_username = {}
localIP= ""
local_port  = 13131


sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
sock.setblocking(True)

while True:
    try:
        sock.bind((localIP, local_port))
        break
    except OSError as oserr:
        print("{} (port {} unreacheable)".format(oserr,local_port))
        local_port = random.randint(1024,65535)

print('Server is running at port {}'.format(local_port))

while True:
    listening(sock)

sock.close()
