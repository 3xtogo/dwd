import socket

# reference: https://realpython.com/python-sockets/
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # s = server
host = socket.gethostbyname(socket.gethostname())
port = 8000
print('connecting to server:' + (str(host) + ' ' + str(port)))
s.connect((host, port))
print('connected to server\ntype message:')


def push_message(r):
    s.send(r.encode())
    data = ''
    data = s.recv(1024).decode()

    print(data)


while 1:
    r = input('')
    print(r)
    push_message(r)

# noinspection PyUnreachableCode
s.close()
print(s)
