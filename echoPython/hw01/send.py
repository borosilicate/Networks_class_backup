import socket
import re
import threading
import time


def conSend(numb):
    con= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.bind(('',int(47644) ))
    con.connect(('nike.cs.uga.edu', int( '47645' ) ) )
    con.send(numb.encode('utf-8'))
    con.send('DONE'.encode('utf-8'))
temp=0
while temp<8:
    temp+=1
    threading.Thread(target=conSend,args=(temp) ).start()
