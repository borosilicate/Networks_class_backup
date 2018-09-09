import sys
import socket
import os
import re
import base64 #was trying to make the png work 
ht="HTTP/1.1"
cL="Content-Length: "
cT="Content-Type: "
cC="Connection: close"
rN="\r\n"
loc='Location: http//'
ok=ht+" 200 OK"+rN+loc
bad=ht+" 400 BAD"+rN+loc
forbid=ht+" 403 FORBIDDEN"+rN+loc
nF=ht+" 404 NOT FOUND"+rN+loc
acptRng='Accept-Ranges: bytes'+rN
PNG='<img alt="Embedded Image" src="data:image/png;base64,'

#all the strings aboce are necesary for sending responses 

#BOOLEAN TO HELP GRADERS WITH DEBUG
check=False

def argCheck(arguments):
    if(check):
        print(len(arguments), "LENGTH")
    if(len(arguments)==3):
        if(check):
            print("length is three")
        if(arguments[1]=="--root"):
            if(check):
                print("Print one is root")
            if(os.path.isdir(arguments[2])):
               if(check):
                   print("two is a valid directory")
                   print("Base Directory for Query is ",arguments[2])
            return arguments[2];
    else:
        print("Base Directory for Query is ","./www")
    return "./www";
    
def query(home,arg):
    
   badOrGood=firstLine(arg)
   badOrGood=str(badOrGood)
   print("QUERRY!!!! after www \n",home+badOrGood)
   if(badOrGood=="bad"):
       temp_file= open('./www/foo.html')
       a=temp_file.read()  
       return bad+'vcf1:47645/foo.html'+rN+cL+str(len(a))+rN+cC+rN+rN+a;
   elif(os.path.isfile( (home+badOrGood) )):
       if(check):
           print("this is good ", home+badOrGood)
       if('..' in (badOrGood)):
           temp_file= open('./www/fot.html')
           a=temp_file.read()
           return forbid+'vcf1:47645/fot.html'+rN+cL+str(len(a))+rN+cC+rN+rN+a;
       #I was getting very weird errors and png was not working ;(
       elif('png' in badOrGood):
           #temp_file= open((home+badOrGood),'rb')
           #a=temp_file.read()
           return ok+'vcf1:47645'+badOrGood+rN+cT+'image/png'+rN+cC+rN+rN;
       else:
           temp_file= open(home+badOrGood)
           a=temp_file.read()
           return ok+'vcf1:47645'+badOrGood+rN+cL+str(len(a))+rN+cC+rN+rN+a;
   elif( os.path.isdir((home+badOrGood)) ):
       if(os.path.isfile((home+badOrGood+'index.html'))):
         temp_file= open(home+badOrGood+'index.html')
         a=temp_file.read()
         return ok+'vcf1:47645/index.html'+rN+cL+str(len(a))+rN+cC+rN+rN+a;
       elif(os.path.isfile((home+badOrGood+'index.txt'))):
           temp_file= open(home+badOrGood+'index.txt')
           a=temp_file.read()
           return ok+'vcf1:47645/index.txt'+rN+cL+str(len(a))+rN+cC+rN+rN+a;
       else:
           temp_file= open('./www/fof.html')
           a=temp_file.read()
           return nF+'vcf1:47645/fof.html'+rN+cL+str(len(a))+rN+cC+rN+rN+a
   else:
       temp_file= open('./www/fof.html')
       a=temp_file.read()
       return nF+'vcf1:47645/Fof.html'+rN+cL+str(len(a))+rN+cC+rN+rN+a
#checks for good arguments in get
#cannot handle options unforutnatly 
def firstLine(args):
    word=mikeP(args)
    #word=word.split(' ')    
   # print(word)
    #print(len(word))
    if(len(word)<5):
        return "bad";
    else:
        # i know this just check for contains but it was best i could time running out at hackathon
        #slow internet 9;50 feels bad man
        if('GET' in word[0] and 'HTTP/1.'  in word[2] ):
            if(check):
                print("GET was there!!!!!!!!!")
            if('Host:' in word[3]   and '47645' in  word[4] ):
               return str(word[1]).strip();
        else:
            return "bad"
                

def mikeP(args):
    let=False;
    j=0;
    x=0;
    six=True
    m=[' ',' ',' ',' ',' ',' ' ]
    while(j<6 and six):
        if(args[x]==' 'or args[x]=='\r' or args[x]==']n'):
            if(let):
                m[j]+=' '
                j+=1
                let=False
            x+=1     
        else:
            m[j]+=args[x];
            let=True
            x+=1
            
        if(j==6):
            six=False;
            return m

            
    


    
