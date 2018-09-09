echo " 0   host =server"&
echo " 1   server_host  =Recieve" &
echo " 2  host connections bytes host:portreciever  filename =sender     " 
if[$1==0]; 
    python3 ftserver.py --port $2:47644
else
    if[$1==1]; then
        python3 ftclient.py --server $2:47644 --receive

    else [$1==2]; then
       python3 ftclient.py --server $2:47644 -c $3 -s $4 --send $5 $6

    fi
fi
fi
