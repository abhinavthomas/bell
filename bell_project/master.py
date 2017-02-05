import socket
import json
import threading
import time
import sqlite3

number_of_devices=1

#data to send
bell_ring = {'data':'ring bell','time':''}
amp_on = {'data':'on amp'}
amp_off= {'data':'off amp'}
#d=bell_ring

#set port and host
port=8888
host=socket.gethostname()
old_time='0'

server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    server_socket.bind((host,port))
except socket.error as msg:
    print 'socket not binding ' ,msg[0],'\n',msg[1]
print 'socket binded to port {0} '.format(host)
server_socket.listen(5)


def send(msg):
    socket_list=[]
    for i in xrange(number_of_devices):
            socket_list.append(sever_socket.accept())
         
    for sockets in socket_list:
            socket[0].send(json.dumps(msg))
            print 'data send : {0} at {1} to {2}'.format(msg['data'],time.localtime(time.time()),sockets[1])


def get_time():
    conn = sqlite3.connect('/home/avinash/bell_web/bell/db.sqlite3')
    c = conn.cursor()   
    c.execute("select name from  app_current")
    s=c.fetchone()
    c.execute("select * from app_bell where name = '"+s[0][0]+"'")
    l = c.fetchall()
    times = [ str(i) for i in l[0]]
    bells = [times[i] for i in xrange(2,15)]
    
    conn.close()
    return str(s[0])

def check_bell():
    new_time = get_time()

    if old_time!=new_time:
        bell_ring['time']=new_time
        send(bell_ring)
        old_time=new_time


while True:
    check_bell()




'''
client_sock,addr=server_socket.accept()
print 'connected with ',addr
client_sock.send(json.dumps(d));
print 'data send : ',d['data']
'''
    
            
    
            




