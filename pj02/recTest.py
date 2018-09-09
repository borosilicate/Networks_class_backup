import socket

udpp="0.0.0.0"
udpt= 47644

soc=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
soc.bind((udpp,udpt))

print("\tConnect \t http://", socket.getfqdn() ,":", soc.getsockname()[1])

while True:
    data, addr = soc.recvfrom(1024)
    print (data)
