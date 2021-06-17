import socket
import threading
import random #랜덤으로 숫자를 얻기 위한 import
from queue import Queue #순번을 알기위한 import

def handler(c,a,send_queue):
    global connections #전역변수
    while True:
        data = c.recv(1024)
        for connection in connections:
            connection.send(bytes(data))
        if not data:
            connections.remove(c)
            c.close()
            break

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(("",2500))
sock.listen(1)
connections = []
send_queue = Queue() #큐

while True:
    c, a = sock.accept()
    cThread = threading.Thread(target=handler, args=(c,a))
    cThread.daemon = True
    cThread.start()
    connections.append(c)
    print(connections)

