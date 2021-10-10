# !/usr/bin/python
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('35.198.208.29',10003))

data = s.recv(999999)
print(data.decode())

while True:
    data = s.recv(999999)
    print(data.decode())
    data = s.recv(999999)
    print(data.decode())

    str = int(eval(data.decode()[data.decode().rfind('\n'):data.decode().find('=')]))
    print(str)

    s.sendall(f"{str}\n".encode())

# ISPCLUB{F45T_a5_71ghtN1n9!!!!}