import socket
from threading import Thread

mySocket = socket.socket()
mySocket.connect("127.0.0.1", 8000)

def sendNumber():
    while True:
        number = input("Введите число: ")
        mySocket.send(number.encode("utf-8"))
        
def getNumber():
    while True:
        ans = mySocket.recv(1024)
        print(ans.decode("utf-8"))

thread1 = Thread(target=sendNumber)
thread2 = Thread(target=getNumber)
thread1.start()
thread2.start()