from socket import *
import threading
import random #랜덤으로 숫자를 얻기 위한 import
from time import sleep  #sleep을 사용하기 위해 import

def send(sock):
    while True:
        Quiz() #퀴즈문제를 제시
        msg = input()
            
        if int(msg) == answer: 
            print("정답입니다.") 
        
        else :  #틀리면 종료
            print("틀렸습니다.")
            break

        try :
            sock.send(msg.encode())
        except:
            print("연결 종료")
            break
    sock.close()

def receive(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                print("연결 종료")
                break
            print(f'Client : {msg.decode()}\n') #여기서 큐를 받아서 client1 이런식으로 할려했으나 실패함
        except:
            print("연결이 종료되었습니다.")
            break
    sock.close()

def Quiz():
    i = random.randint(2,9) #랜덤 변수 2~9
    j = random.randint(2,9) #랜덤 변수 2~9
    global answer
    answer = i*j
    
    print("구구단을 외자!")
    sleep(1)
    print(i,'*',j)


if __name__ == '__main__':
    sock = socket(AF_INET,SOCK_STREAM)
    sock.connect(("localhost",2500)) #IP주소와 Port를입력함
    
    cThread = threading.Thread(target=send,args=(sock,))
    cThread.daemon = False
    cThread.start()
    sThread = threading.Thread(target=receive,args=(sock,))
    sThread.daemon = False
    sThread.start()

