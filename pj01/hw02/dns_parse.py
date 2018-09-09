import sys      #argument 
import os
import getopt
import shutil
import io
import struct 

def intm(numstr):
    if("a"==numstr):
        return 10;
    elif("b"==numstr):
        return 11;
    elif("c"==numstr): 
        return 12;
    elif("d"==numstr):
        return 13;
    elif("e"==numstr):
        return 14;
    elif("f"==numstr):
        return 15;
    else:
        return int(numstr);
#QUERY TYPE
def opt(numb):
    if(numb>5 or numb==0):
        return "QUERY"
    elif(numb==1):
        return "IQUERY"
    elif(numb==2):
        return "STATUS"
    elif(numb==3):
        return "RESERVED"
    elif(numb==4):
        return "NOTIFY"
    elif(numb==5):
        return "UPDATE"
#z error
def zE(numb):
    if(numb==0):
        return "NO ERROR="+str(numb)
    else:
        return "ERROR="+str(numb)

#def qType(data,fZero):

def qName(data):
    top=data[0];
    print("<<DNS QUESTION START")
    num=intm(top[40]) + intm(top[41]);
    row=0;
    ofset=38
    stringg="";
    if(num>1):
        stringg+=(str(top[38])+str(top[39])+" " )
        num=num-1;
    notDone=True;
    while( notDone ):
       ofset+=5; 
#       print(ofset,":ofset plus 3=", ofset+3, "ROW:",row," LEN TOP:",len(top) )
       if(num>=1):
           b3=top[ofset+2]; b4=top[ofset+3]; b1=top[ofset]; b2=top[ofset+1];
           if(b3==" " or b1==" " or b4==" " or b2==" " or top[ofset+2]=="0" or top[ofset+3]=="0"):
               notDone=False;
           else:
               stringg+=(str(top[ofset+2])+str(top[ofset+3])+" "+str(top[ofset])+str(top[ofset+1])+" " )
           num-=1;
       elif(num==1):
           num=intm(top[ofset+2])<<4+intm(top[ofset+3]);
           stringg+=str(top[ofset])+str(top[ofset+1])+" "
           num-=1;
           
       if(ofset==43):
           row+=1;
           if(row>len(data)-1):
               notDone=False;
           else:
               top=data[row];
           ofset=3;
    z=0
    #print(stringg)
    name=""
    temp=""
    while(z<len(stringg)):
        if(intm(stringg[z])>=10):
            z+=6;
        else:
            if(stringg[z]=="0"):
                name+="."
            else:
                temp=str( bytearray.fromhex(stringg[z]+stringg[z+1]+stringg[z+2]).decode()  )
                name+=temp
            z+=3;
    print("Resource Record Name:",name)
    print(ofset)
    ofset=3;
    row=1
    print(row)
    top=data[row]
    rt=intm(top[ofset+6])
    print("Resource Type:",rt)
    
    print(data[0]);
    print(data[1]);
    print(data[2]);
    print(data[3]);
    
    

#prints header info by bit minipulation
def header(data):
    top=data[0]
    print("<<<HEADER INFO")
    id1=(intm(top[8])<<4)+(intm(top[9]))+(intm(top[10])<<12)+ (intm(top[11])<<8 );
    print("ID:",id1  ) 
    byte3=intm(top[15]); byte4=intm(top[16]);
    qr=(byte3&8)>>3;  op=byte3%8<<1+( (byte4&8) >>3);
    aa=byte4&4>>2; tc=byte4&2>>1; rd=byte4&1;
    print("QR:",qr," OPCode:",opt(op)," AA:",aa," TC:",tc," RD:",rd )
    byte5=intm(top[13]); byte6=intm(top[14]);
    ra=byte5&8>>3; z=byte5%8; rcode=byte6;
    print("RA:",ra," Z:",zE(z)," RCode:",rcode)
    qtotal=(intm(top[18])<<4)+(intm(top[19]))+(intm(top[20])<<12)+ (intm(top[21])<<8 );
    print("Question Count:",qtotal)
    antotal=(intm(top[23])<<4)+(intm(top[24]))+(intm(top[25])<<12)+ (intm(top[26])<<8 );
    print("Answer Record Count:",antotal)
    nstotal=(intm(top[28])<<4)+(intm(top[29]))+(intm(top[30])<<12)+ (intm(top[31])<<8 );
    print("Athority Record Count:",nstotal)
    arcount=(intm(top[33])<<4)+(intm(top[34]))+(intm(top[35])<<12)+ (intm(top[36])<<8 );
    print("Additional Record Count:",arcount)
    print("<<<END HEADER INFO\n")
    qName(data);



if(len(sys.argv)<2):
    print("Sorry needs file input.");
    exit(0);
else:
    print(sys.argv[1]);
    if( not os.path.isfile(sys.argv[1]) ):
        print("bad file name");
        exit(0);
    else:
        strs= "";
        with open('temp.txt',"r") as f:
             data=f.readlines() 
        print(data[0])
        print(data[1])
        print(data[2])
        header(data)
        
exit(0)
