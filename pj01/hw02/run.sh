#gets rid of old hex
rm temp.txt

#if no file
if [  "$#" -ne 1  ];  then
 echo "no file ???" 
else
hexdump $1 >> temp.txt
python3 dns_parse.py $1
fi