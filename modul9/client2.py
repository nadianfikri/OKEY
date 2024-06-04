import socket

s = socket.socket()
ip = input(str("Masukkan alamat IP server: "))
name = input(str("Masukkan username: "))
port = 2222
s.connect((ip, port))
s.send(name.encode())
c = (s.recv(100))
print(c.decode())

while True:
    a = input(str("Masukkan pesan: "))
    b = str.encode(a)
    s.send(b)
