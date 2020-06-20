loop = True
adminusr = ['client1','client2]
adminpass = ['1234']
globalcalluser = "server"

def client():
    import socket

    listenerSocket = socket.socket()
    serverIP = "0.0.0.0"
    serverPort = 2222
    listenerSocket.bind((serverIP,serverPort))
    listenerSocket.listen(0)
    print 'server siap menerima client'

    while True:
        handlerSocket, addr = listenerSocket.accept()
        print 'sebuah client baru terkoneksi dengan alamat : ',addr
        while True:
            message = raw_input("masukkan pesan anda : ")
            handlerSocket.send(message)
            pass
        pass

while(loop):
        print 'login server'.upper()
        input1 = raw_input("Username = ")
        input2 = raw_input("Password = ")

        if ((input1 in adminusr) and (inputB in adminpass)):
            globalcalluser = input1
            server()
        else:
            print 'maaf username atau password yang anda masukkan salah'
            loop