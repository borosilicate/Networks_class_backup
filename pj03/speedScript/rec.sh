echo "Which Port to listen on? \n"

read port

echo "\t New file Name? \n"

read fileName

echo 'Waiting for connection to '+$port 

time nc -l $port > $fileName

