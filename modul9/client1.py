import time, socket

def Awal():
    print("Selamat bergabung pada Chatroom")
    print("Inisialisasi....\n")
    time.sleep(1)

def Inisialisasi():
    host = input(str("Masukkan alamat IP server: "))
    name = input(str("Masukkan username: "))
    port = 1234
    print("Mencoba terkoneksi pada ", host, "(", port, ")")
    time.sleep(1)
    s.connect((host, port))
    print("Tersambung...\n")
    s.send(name.encode())
    s_name = s.recv(1024)
    s_name = s_name.decode()
    print(s_name, "telah bergabung pada Chatroom\nKetikkan [e] untukkeluar dari Chatroom\n")
    Koneksi(s_name)

def Koneksi(nama):
    while True:
            message = s.recv(1024)
            message = message.decode()
            print(nama, ":", message)
            message = input(str("Me : "))
            if message == "[e]":
                message = "Meninggalkan chat room!"
                s.send(message.encode())
                print("\n")
                break
            s.send(message.encode())

if __name__ == '__main__':
    s = socket.socket()
    shost = socket.gethostname()
    ip = socket.gethostbyname(shost)
    print(shost, "(", ip, ")")
    Awal()
    Inisialisasi()