import socket
import _thread
import threading
import sys
import os
from ftp import ( askS )
import time
# id== get id  iddone== done and remove host:port= send host port back
connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
CLIENTPORT=47644
if('-p' in sys.argv):
    f=sys.argv.index('-p')+1
    CLIENTPORT=int(sys.argv[f] )
if('--port' in sys.argv):
    f=sys.argv.index('--port')+1
    CLIENTPORT=int( sys.argv[f] )
buff=4096
if('-s' in sys.argv ):
    f=sys.argv.index('-s')+1
    buff=sys.argv[f]
if('--size' in sys.argv):
    f=sys.argv.index('--size')+1
    buff=sys.argv[f]
print(connection," BEFORE BIND ONE")
connection.bind(('',CLIENTPORT)) #47645 is the server
#connection.listen(10)
#print("command to connect:", socket.getfqdn() , connection.getsockname())
#print(connection,":::connection")
serverName=sys.argv[2]; middle=':';
serverH,middle,serverP= serverName.partition(middle)
#print(  serverName.partition(middle) )
serverH=serverName.partition(middle)[0] 
serverP= serverName.partition(middle)[2]
#print(serverH, serverP)
typeC=sys.argv[3]# DECIEDES IF --receive or if -c is sending
if('--receive' in sys.argv ): #SET
    print("Buffer Size set to ",buff,"!")
    print("Using port",CLIENTPORT,"!")
    print("Asking '",serverName,"' about an identification number...")
    idd=ftp.askS('id',serverH,serverP,connection)
    connection.shutdown(1)
    connection.close()
    con= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if(CLIENTPORT==47644):
        con.bind(('',47645))
    elif(CLIENPORT==47645):
        con.bind(('',47644))
    con.listen(5)
    print("Issued",idd,"' for identification...")
    print("WAITING FOR CONNECTION")
    (clientsocket, address) = con.accept()
    FILE=( con.recv(64) ).decode('utf-8') 
    CNUM=( ( con.recv(64) ).decode('utf-8') )
    if(os.path.isfile(FILE) ):
        print(FILE, "it exists already")
    else:
        print("Receiving '",FILE,"' over ",CNUM," connections...")
        #ftp.recvAll(FILE,con, CNUM)
elif('--send' in sys.argv):
    CNUM=int(sys.argv[4])
    ID= sys.argv[8]
    FILE=sys.argv[9]
    print("Asking '",serverName,"' about '",ID,"'..." )
    idd=ftp.askS(ID,serverH,serverP,connection)
    print(connection, "BEFORE CLOSE")
    connection.shutdown(1)
    connection.close()
    time.sleep(3)
    connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(connection,"BEFORE BIND")
    #connection.bind(('',CLIENTPORT))    
    print(connection,"AFTER CLOSE CONNECTION")
    clientH=serverName.partition(middle)[0]
    clientP= serverName.partition(middle)[2]
    print("Found client at '",idd,"'...") 
    #FAULTY 
"""
    if(os.path.isfile(FILE)):
        if(int(clientP)==int(47644)):
            try:
                connection.connect((clientH,47645) ) 
            except(ConnectionRefusedError):
                print("Connection Failure:",connection)
                
        elif(int(clientP)==int(47645)):
            try:
                connection.connect((clientH,47644) )
            except(ConnectionRefusedError):
                print("Connection Failure:",connection)
        print(connection)
        connection.sendall((FILE).encode('utf-8'))
        connection.sendall(str(CNUM).encode('utf-8') )
        print("READY TO SEND ALL!")    
  #ftp.sendALL(CNUM,buff,connection,FILE)
    else:
        print("No file Named ",FILE)
"""

def recc(c, addr):
    fileName="temp.txt"
    dat=c.recv(4096)
    fileName=(dat).decode("utf-8")
    print(fileName,":~filename~")
    if( os.path.exists(fileName) ):
        print("Already file!")
        print("Transfer Failed")
    else:
        print("Receiving '",fileName,"'...")
        ftp.makeFile(c,fileName)
        print("Transfer complete!")

#def scriptCat(CNUM,connection):
    
        

#start
def start(serverH,serverP,connection):
    middle=":"
    print(typeC,"TYPE")
    if('--re' in sys.argv ):
        print("IN SEND",sys.argv[4])
        ID=sys.argv[4]
        clientH,middle,clientP=ID.partition(middle)
        iddd=ID.partition(middle)[0]
        iddd=socket.gethostbyname (iddd)
        iddd+=":"
        iddd+=ID.partition(middle)[2]
        print("iddd",iddd)
        print("Asking '",serverName,"about ",ID ,"...")
        idd='vcf3:47644'
        #connect to server
        print("attempting to connect...",serverH,int(serverP) )
        print("host:",socket.getfqdn(serverH) )        
        connection.connect( (serverH,int(serverP)) )
        connection.sendall(iddd.encode('utf-8'))
        idd=connection.recv(256)
        connection.close()
        con=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #con.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        con.bind(("0.0.0.0",47645)) #47645 is the server                                                                                
        #con.listen(1)
        one=str((ID.partition(middle))[0])
        two=int(ID.partition(middle)[2])
        print( str(ID.partition(middle)[0]) , int(ID.partition(middle)[2]) )
        con.connect((one,two))
        print("idd:",idd.decode('utf-8'))
        if(True):
            print("Found client at '",socket.gethostbyname_ex(clientH),middle,clientP,"'..." )
            fileName1=sys.argv[5]
            if( os.path.isfile(fileName1) ):
                if("/" in fileName1):
                    ftemp=fileName1.split("/")
                    print(ftemp[len(ftemp)-1], len(ftemp))
                    fileName2=ftemp[len(ftemp)-1]
                    print(fileName2)
                else:
                    fileName2=fileName1
                print("Sending '",fileName2,"'...")
                ftp.sendName(con,fileName2)
                ftp.sendFile(con,fileName1)
            else:
                print("file not found!")           
        elif('no' in idd.decode('utf-8') ):
           print("client not connected")
            
    elif(typeC in " --receive  --recieve "):
        print("IN RECEIVE")
        print("Asking '",serverName,"' about an identification number...")
        print("Asking '" ,serverH+":"+serverP,"' about an identification number...")
        idd="vcf3:47644"
    #get ID from server is own name...
        if('.'not in serverH):
            serverHH=socket.gethostbyname(serverH)
        print(serverH,":serverHost  serverPort:",serverP)        
        connection.connect((serverH, int(serverP)))
        connection.sendall( ("id").encode("utf-8"))
        idd=(connection.recv(4096)).decode("utf-8")
        print("Issued '",idd,"' for identification...")
        connection.close()
        con=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        con.bind(("0.0.0.0",47644)) #47645 is the server 
        con.listen(1)
        print(connection)
        print(con)
        while True :
            c, addr = con.accept()
            
            _thread.start_new_thread(recc,(c,addr) ) 
        c.close()
        connection.close()


# start(serverH,serverP,connection)
#_thread.start_new_thread(start,("nothing","something"))
#connection.close()
