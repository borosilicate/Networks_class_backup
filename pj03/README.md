michael hearn mjh55154@uga.edu

file transfer client 


activete venv: source bin/activate #NEEDED TO WORK!!!

to run: python3 ftserver.py --port port   

to run clients: 
				#Use right number VCF!
python3 ftclient.py --server vcf(1-5):47645 --receive
 python3 ftclient.py --server HOST:PORT [-s SIZE] [-p PORT] --receive 


                                ID=vcfRECIEVER#:47644 
OLD:python3 ftclient.py --server vcf(1-5):47645 --send ID fileExample.txt
NEW:python3 ftclient.py --server vcf(1-5):47645 -c CNUM -s SIZE --send ID fileExample.txt
	    			 		 number of parrallell connections
						-size of buffer of reciever

# added nc application in speedScript



can handle diffrent folder as long as its bellow *
format should be /folder/nextfolder/filename


