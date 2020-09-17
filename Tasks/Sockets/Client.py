import socket

sock = socket.socket()
sock.connect(('localhost', 9090))

while True:
    text = input('===')
    if text == 'exit':
        break
    sock.send(text.encode())
    try:
        data = sock.recv(1024)
    except ConnectionAbortedError:
        print('Server is dead')
        break
    print(data.decode())

sock.close()
