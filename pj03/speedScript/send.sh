echo 'Host name?'

read host

echo "port to send to ? "

read port

echo "file to send ?"

read fileName

time nc $host $port < $fileName


