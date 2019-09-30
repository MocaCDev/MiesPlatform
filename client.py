import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.40.10.1',1234))

msg = s.recv(8)
print(msg.decode("utf-8"))
