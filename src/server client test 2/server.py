import socket

class SERVER:
#reference: https://realpython.com/python-sockets/
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname(socket.gethostname())
port = 8000

serversocket.bind((host,port))

serversocket.listen(5)
print('SERVER:\nserver startet listening')

while 1:
    (clientsocket, address) = serversocket.accept()
    print ("connection found!")
    while 1:
        data = clientsocket.recv(1024).decode()
        print ('message recieved!\nmessage:'+data)
        print('sending back recieved!')
        ack= 'message recieved!'
        clientsocket.send(ack.encode())

