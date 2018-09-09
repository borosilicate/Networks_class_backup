import socket   #its a server so needed
import _thread #concurrency
import random   #random
import sys      #argument   
import http  #mylist of 
 
connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
connection.bind(("0.0.0.0",47645))
connection.listen(10)

qDirectory="./www"
print("\tConnect \t http://", socket.getfqdn() ,":", connection.getsockname()[1])
""" Putting some other defs http.py
argCheck(arguments from command line):
this function changes default directory if --root is third command and 
the fourth arg is a valid directory 
******
firstLine(get message)
function parses and sends bad if bad or file/directory if good
******
query(home default, argument either bad or inquiry)
returns message to incode 
"""

def runn(client, adress):
    #GET  message
    data=client.recv(47645)
    #Print to SERVER
    print (data.decode('utf-8'))
    message=http.query(qDirectory,data.decode('utf-8'))
    if('image/png' in message):
        badOrGood=http.firstLine(data.decode('utf-8'))
        badOrGood=str(badOrGood)
        print('@@@'+(qDirectory+badOrGood)+'@@@@@')
        print('sorry images arnt printing errors')
        """   
        hearn@nike:~$ display: unable to open image `/home/ugrads/hearn/L17215-9849TMP.png': 
        No such file or directory @ error/blob.c/OpenBlob/2589.display: 
        unable to open file `/home/ugrads/hearn/L17215-9849TMP.png' @ error/png.c/ReadPNGImage/3639.
        """
        temp_file= open((qDirectory+badOrGood),'rb')
        a=temp_file.read()
        client.send(message.encode('utf-8'))
        client.send(a)
    else:
        client.send(str(message).encode('utf-8'))
    client.shutdown(socket.SHUT_RDWR)
    client.close()

while True:
    #change root/ try
    qDirectory=http.argCheck(sys.argv);
    client, adress = connection.accept();
    _thread.start_new_thread(runn,(client,adress))
connection.close()
