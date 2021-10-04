# !/usr/bin/python
import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('35.198.208.29',10002))

data = s.recv(999999)
print(data.decode())

while True:
    data = s.recv(999999)
    print(data.decode())
    data = s.recv(999999)
    print(data.decode())
    # if 'CTF{'.encode() in data:
    #     break
    i = data.index('quest: '.encode())
    d = data[-12:-3].decode()

    str = eval(d)
    print(str)

    s.sendall(f"{str}\n".encode())

# ISPCLUB{m4th_f0R_dUmm13S!!!!!!!}