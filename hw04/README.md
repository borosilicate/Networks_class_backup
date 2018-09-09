michael hearn mjh55154@uga.edu

filte transfer client 


activete venv: source bin/activate

to run: python3 ftserver.py 

to run clients: 
				#Use right number VCF!
python3 ftclient.py --server vcf(1-5):47645 --receive

                                ID=vcfRECIEVER#:47644 
python3 ftclient.py --server vcf(1-5):47645 --send ID fileExample.txt

can handle diffrent folder as long as its bellow *
format should be /folder/nextfolder/filename


