import socket

host = socket.gethostname()
port=8888
clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'socket created'
clientsock.connect((host,port))
def func():
   
    clientsock.send(raw_input('enter message:'))
    print 'data send'
    print clientsock.recv(1024)

if __name__=="__main__" :
    while True:
            func()
    

    
