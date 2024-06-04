import socket
import threading

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
port = 2222
ip = ""
s.bind((ip, port))
s.listen()
print("Server sudah hidup. Menunggu koneksi masuk...")

def Koneksi(name, session, addr):
    print(addr)
    session.send("Server connected".encode())
    while True:
            data = session.recv(100)
            print(name +"("+ addr[0] + "):" + data.decode())

while True:
    session , addr = s.accept()
    s_name = session.recv(1024)
    s_name = s_name.decode()
    t = threading.Thread(target=Koneksi, args=(s_name, session, addr))
    t.start()
