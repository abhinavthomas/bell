# code for server
import socket
import sys

port = 8888
host = socket.gethostname()
print host

serversock=socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print 'socket created'

try:
        serversock.bind((host,port))
except socket.error as msg:
        print 'binding port failed\n',str(msg[0]),'message: ',str(msg[1])
        sys.exit()

print 'bind complete'

#starting listening

serversock.listen(3)
print 'socket listening'

while True:
            clientsock,addr=serversock.accept() #blocking call
            print 'conneceted with ',addr;
            while True:
                data=clientsock.recv(1024)
                if not data : break
                print data
                clientsock.send(data+'......ok')

serversock.close()


        

