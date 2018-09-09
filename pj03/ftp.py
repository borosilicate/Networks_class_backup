import subprocess
import socket
import sys
import os
import shutil
import time
import threading
import math
import re
from multiprocessing.dummy import Pool as ThreadPool
#filename connection
#sendName(con,filename) send fileName to con
#getFileName(con) decoded filename
def getFile(con,connections, size):
    pool=ThreadPool(size)                  
    t0=time.time()
    #esults=pool.map(functionName, myArray)
    t1=time.time()
    print("start:",t0)
    print("end:",t1)
    total=t1-t0
    print("Time:",total)
    #endtimer

def sendFile(con, fileName,conAmount):
    if(os.path.isfile(fileName) ):
        f=open(fileName, "r+")
        shutil.copy2(fileName,"*" )
        con.sendall(f)
        f.close()
        print("DONE SENDING")
    else:
        print("Path to file does not exist")
        
#takes connection and fileName then
def makeFile(con,fileName):
    if('/' in fileName):
        print("contains /")
    else:
        print("Receiving '",fileName,"'...")
        filee=open(fileName,"ab+")
        recvFile(con,fileName,filee)

def  getFileName(con):
    return (con.recv(4096)).decode("utf-8")
#recvFile recievies and writes to a filee
def recvFile(con,fileName,filee):
    con.settimeout(5)
    try:
        data=b''
        dataa=b''
        while len(dataa)==len(data) or len(dataa)==4096:
            dataa = con.recv(4096)
            filee.write(dataa.decode('utf-8'))
            data=data+dataa;
    except socket.timeout:
        print(";; connection timed out; no server data recieved")
#sendName to connection
def sendName(con,fileName):
    con.sendall(fileName.encode("utf-8"))

#def mkfilee(filenm,bytear):
    #filee=()


def breakFile(numb,fileName):
    result=subprocess.run(['wc', '-c', fileName], stdout=subprocess.PIPE)
    result=result.decode('utf-8')
    result=int ( re.search(r'\d+', headline).group() )
    result+=1;
    obj=[]
    temp=b''
    with open(fileName, "rb") as f:
        byte = f.read(1)
        while byte != b"":
            temp+=byte
            if(len(temp)==result):
                obj.append(temp.encode('uft-8'))
                temp=b''
                byte = f.read(1)
    f.close()
    return obj

def askS(strg,serverH,serverP,connection):
    print(serverH,":SH  SP:",serverP)
    connection.connect( (serverH,int(serverP) ) )
    connection.sendall(strg.encode('utf-8'))
    return (connection.recv(256)).decode('utf-8')
    
# send                                                                                                                                                                                   
#   python3 ftp.py 47644 127.0.01 47645 2 ftp.py 4096                                                                                                                                    
def client_r(socket,numb , buff):
    filee='temp'+ascii(numb)
    f = open(filee, 'rb+')
    b=b''
    b=socket.recv( int(buff) )
    while(b!=b''):
        f.write(b)
        b=socket.recv( int(buff) )
def client_s(con,host,port,file):
    print("clientSend host port ",host," ", port)
    con.connect((host, int(port) ) )
    f=open(file,'w+')
    con.send(f.read())

print("1=por  2=rec-host 3=rec-port 4=#sendcons0recieve 5=file 6=buff")
connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if(int(sys.argv[4])>0): #sending                                                                                                                                                         
    connection.bind(('',int(sys.argv[1]) )) # send port                                                                                                                                  
    if(os.path.isfile(sys.argv[5]) ):
        output = subprocess.check_output('wc -c '+sys.argv[5] , shell=True)
        output=output.decode('utf-8')
        print(output,"output")
        out=re.search(r'\d+', output).group()
        bytes=math.ceil( int(out)/int(sys.argv[4]) )
        output = subprocess.call('split '+str(bytes)+' '+sys.argv[5] , shell=True)
        temp=0;
        max=int(int(sys.argv[4])-1)
        front='xa'
        end_char=97
        tim=time.clock()
        while(temp<max):
            client_s(connection,sys.argv[2], sys.argv[3],front+chr(end_char+temp))
            temp+=1
        aft=time.clock()
        print('diff=',aft-tim)


elif(int(sys.argv[4])==0): #recieving                                                                      
    connection.bind(('',int(sys.argv[3]) )) # recv port                                      
    connection.listen(int(sys.argv[4])+1)
   # (clientsocket, address) = serversocket.accept()          
   # name=recv(20)
   # cons=recv(20) 
    j=0;
    bef=time.clock()
    cons=int ( sys.argv[4] )
    print(j," < ",cons)
    while j<cons:
        print('about to recv:',j)
        (clientsocket, address) = connection.accept()
        ct = client_r(clientsocket, j, sys.argv[6])
        ct.run()
        j+=1




