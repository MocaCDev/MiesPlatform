import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((s.gethostname(), 1236))
s.listen(5)

while True:
    clientsocket, adress = s.accept()
    print(f'Connection from {adress} has been established')
    
    msg = "Welcome to the server!"
    msg = f'{len(msg):<{HEADERSIZE}}' + msg
    
    clientsocket.send(bytes(msg,"utf-8"))
