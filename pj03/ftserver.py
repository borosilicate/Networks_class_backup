import socket
import _thread
import sys
import os
import re
import base64
import re
idList=[''];
connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
SPORT=47645
if(len(sys.argv)<2):
    connection.bind(('',SPORT))
else:
    SPORT=int(sys.argv[2])
    connection.bind(('',SPORT))
connection.listen(10)
print("command to connect:", socket.getfqdn() , connection.getsockname())
#print(connection)
print("host:",socket.gethostbyname_ex( socket.getfqdn() ))
def addRec(client, adress):
    print("client",client,adress)
    data =client.recv(47645);
    data=data.decode('utf-8')
    print(data,":DATA")
    if(data=="id"):
        print(client,"::<<client ")
        print("adress::>>",adress)
        print("adress ZERO",adress[0])
        print("adress ONE",adress[1])
        cs=adress[0]+':'+str(adress[1])
        print(cs,":the port is the id ;D")
        idList.append(cs)
        idd=cs.encode('utf-8')
        client.send(idd)
        #client.close()
    elif(data=="iddone"):
        cs=client.getsocketname()
        cs=str(cs[1])
        print(cs)
        if(cs in idList):
            idList.remove(cs)
        else:
            print(cs,":can't remove// not there")
        #client.close();
    elif(':' in data):
        print(data)
        print(idList)
        if(data in idList):
            client.send(data.encode('utf-8'))
            #client.close()
             #client.send(kk);
             #data =client.recv(47645);
        else:
            client.send(("no").encode("utf-8"))
            #client.close()
            print(data," :not recieving currently")    
        #client.close()

while True:
    client, adress = connection.accept();
    print(client,adress)
    _thread.start_new_thread(addRec,(client,adress))
connection.close()
