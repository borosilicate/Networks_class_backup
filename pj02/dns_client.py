import socket   #its a server so needed
import _thread #concurrency
import random   #random
import sys      #argument   
import http  #mylist of 

#creating http def argvTcpCheck(sys.argv): returns true or false
http.printArgv(sys.argv )
tcpp=False;
port=47645;
localHost=socket.getfqdn()
if http.argvCheck(sys.argv, "--tcp"):
    tcp=True
    connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)#TCP
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    connection.bind(("0.0.0.0",47645))
    #connection.listen(2)
else:
    connection= socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
    connection.bind(("0.0.0.0",47645))
    #connection.listen(10)

# print("\tConnect \t http://", socket.getfqdn() ,":", connection.getsockname()[1])
#print("\t ", sys.argv[0],".",sys.argv[1],".",sys.argv[2],".");
""" Putting some other defs http.py            """
#except connection.timeout as e:
#    print(";; connection timed out; no servers could be reached")
    
def runn(argv, con):
     #set variables in http->send message
    """ This takes in the line args and forms the message and sends the message as well to the desired host"""
    #decided to just print info inside setSend easier
    data=http.setSend(argv,connection);
    #con.shutdown(socket.SHUT_RDWR)
    con.close()

    #change root/ try                                                                                       
    #qDirectory=http.dnsargCheck(sys.argv);                                                                 
    #client, adress = connection.accept();     #_thread.start_new_thread(runn,(client,adress)) 

runn(sys.argv, connection)
connection.close()
