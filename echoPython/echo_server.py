import socket
import threading
import _thread
connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
connection.bind(("0.0.0.0",47645))
connection.listen(10)
print("command to connect: telnet ", socket.getfqdn() , connection.getsockname()[1])
knock="KNOCK KNOCK\n"
kk = knock.encode('utf-8')
who="WHO'S THERE?\r\n"
w=who.encode('utf-8')
def start(client ,adress):
    client.send(kk)
    data =client.recv(47645)
    while data!=(w):
         client.send(kk)
         data =client.recv(47645)
         print('received {} of length {}'.format(data, len(data)))
    # print('received {} of length {}'.format(data, len(data)))
    client.send(data)
    client.shutdown(socket.SHUT_RDWR)
    client.close()
  #  print('Hello "WORLD" \'ESCAPE\' ')


while (True):
    client, adress = connection.accept()
    _thread.start_new_thread(start,(client, adress))
    
