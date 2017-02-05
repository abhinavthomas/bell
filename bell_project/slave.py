import socket
import json
import time
import threading

#add host and port
host=socket.gethostname()
port=8888


client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def ring_bell(n_time):
    current_time=time.localtime(time.time());
    hour=int(current_time[3])
    mn=int(current_time[4])
    next_hour=int(n_time[0:2])
    next_min=int(n_time[3:5])
    delay=((next_hour-hour)*60*60)+(next_min-mn)*60
    time.sleep(delay)
    print "bell rang at",n_time
 
def on_amp():
    print 'amp on at',time.asctime(time.localtime(time.time()))
    

def off_amp():
    print 'amp off at',time.asctime(time.localtime(time.time()))

def check_msg(ms):
     s = str(msg['data'])
    
     if s == 'on amp':
            on_amp()
            print 'amp onned'

     elif s == 'off amp':
            of_amp()

     elif s == 'ring bell':
            ring_bell(msg['time'])
     

connect=0

while True:

        try:
            client_socket.connect((host,port))
            connect=1;
        except socket.error:
            pass
            
        if connect:
            connect=0
            msg=json.loads(client_socket.recv(4096))
            print msg['data']
            t = threading.Thread(target=check_msg,args=(msg,))
            t.start()

        
        
                
        




    
   

