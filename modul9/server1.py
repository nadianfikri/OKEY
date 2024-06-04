import time, socket

def Awal():
    print("Selamat bergabung pada Chatroom")
    print("Inisialisasi...\n")
    time.sleep(1)

def Inisialisasi():
    s.bind((ip, Port))
    print(host, "(", ip, ")")
    name = input(str("Masukkan username: "))

    s.listen(100)
    print("Menunggu koneksi masuk...")
    conn, addr = s.accept()
    print("Menerima koneksi dari ", addr[0], "(", addr[1], ")")
    
    s_name = conn.recv(1024)
    s_name = s_name.decode()
    print(s_name, "Sudah terkoneksi kedalam chatroom\nKetik [e] untukkeluar dari chatroom\n")
    conn.send(name.encode())
    Koneksi(conn, s_name)

def Koneksi(konek, nama):
   while True:
        message = input(str("Me: "))
        if message == "[e]":
            message = "Meninggalkan chatroom"
            konek.send(message.encode())
            print("\n")
            break
        konek.send(message.encode())
        message = konek.recv(1024)
        message = message.decode()
        print(nama, ":", message)

if __name__ == '__main__':
    s = socket.socket()
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    Port = 1234
    Awal()
    Inisialisasi()