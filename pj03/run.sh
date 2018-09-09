"""
server=  0  port#
recieve= 1  host port
send=    2  host  councount#  Size#    vcf?:port?#  ID# $fileName

"""

if[$1==0]; then
python3 ftserver.py --port $2
else
    if[$1==1]; then
	python3 ftclient.py --server $2:$3 --receive
	
    else [$1==2]; then
       python3 ftclient.py --server $2:$3 -c $4 -s $5 --send $6 $7