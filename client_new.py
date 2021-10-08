import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    send_msg = input("Ваш ответ: ")
    client.sendto(send_msg.encode("utf-8"), ("localhost", 8083))
    if send_msg == "exit":
        break
    back_msg = client.recv(1024).decode("utf-8")
    print("Ответ от сервера: ", back_msg)
client.close()