
def rest(numb,d,recs):
#    print(d)
    #print(d[numb],d[numb+1])
    # end=''                                                                                                                                                  
    if(recs>0):
        ln=doubleZero(d,numb+2)
        typeIs=intToType( intm(d[ln+2])*16+intm(d[ln+3]) )
        ttyl=addHex(d,ln+9,8)
        #print(d[ln+9:ln+9+8])
        print(dehex(numb,d).decode("utf-8"),"\t",ttyl,"\tIN\t",typeIs,"\t",end='' )
        if(typeIs=='A'): #GOOD
            print(addHex(d,ln+20,1),".",addHex(d,ln+22,1),".",addHex(d,ln+24,1),".",addHex(d,ln+26,1))
            rest(ln+28, d,recs-1)
        elif(typeIs=='NS'): #GOOD
            print(dehex(ln+20,d).decode("utf-8"))
            #print(d[ln+16],d[ln+17],d[ln+18],d[ln+19])
            ofset=addHex(d,ln+16,3)*2+20
            #print(d[ofset+ln],d[ofset+ln+1])
            rest(ln+ofset,d,recs-1)
        elif(typeIs=='CNAME'):
            end=doubleZero(d,ln+2)
            print(dehex(ln+20,d).decode("utf-8"),end='')
            print(dehex(end,d).decode("utf-8"),end='')
            ofset=addHex(d,ln+16,3)*2+20
            print(addHex(d,ofset,8),end=''); 
            ofset+=8
            print(addHex(d,ofset,8),end='');
            ofset+=8
            print(addHex(d,ofset,8),end='');
            ofset+=8
            print(addHex(d,ofset,8),end='');
            ofset+=8
            print(addHex(d,ofset,8));
            ofset+=8
            rest(ofset, d,recs-1)
        elif(typeIs=='SOA'):
            end=doubleZero(d,ln+2)
            print(d[ln+20],d[ln+21])
            print(dehex3(ln+20,d,addHex(d,ln+20-4,3)).decode("utf-8"),end='')
#            print(dehex(end,d).decode("utf-8"),end='')
            ofset=addHex(d,ln+16,3)*2+20
            print(addHex(d,ofset,8),end='');
            ofset+=8
            print(addHex(d,ofset,8),end='');
            ofset+=8
            print(addHex(d,ofset,8),end='');
            ofset+=8
            print(addHex(d,ofset,8),end='');
            ofset+=8
            print(addHex(d,ofset,8),end='');
            """aft=doubleZero(d,ln+20)
            print(d[aft:aft+10], end='')
            print(dehex(ln+26,d).decode("utf-8"),end='')
            print( dehex(aft,d).decode("utf-8") )
            ofset=addHex(d,ln+16,3)*2+20+40
            rest(ofset, d,recs-1) """
        elif(typeIs=='WKS'):
            ofset=addHex(d,ln+16,3)*2+20
            rest(ofset, d,recs-1)
        elif(typeIs=='PTR'):
            ofset=addHex(d,ln+16,3)*2+20
            rest(ofset, d,recs-1)
        elif(typeIs=='HINFO'):
            ofset=addHex(d,ln+16,3)*2+20
            rest(ofset, d,recs-1)
        elif(typeIs=='MINFO'):
            ofset=addHex(d,ln+16,3)*2+20
            rest(ofset, d,recs-1)
        elif(typeIs=='MX'):
            ofset=addHex(d,ln+16,3)*2+20+4
            print(dehex(ln+24,d).decode("utf-8"))
            rest(ofset, d,recs-1)
        elif(typeIs=='TXT'):
            ofset=addHex(d,ln+16,3)*2+20
            rest(ofset, d,recs-1)
        elif(typeIs=='ANY'):
            print(';;')

#SOA MAGIC
def soaString(size,d,firstChar):
    if(d[firstChar]=='c' and  d[firstChar+1]=='0'):
        return  dehex(intm(firstChar+1)+intm(firstChar+2)+intm(firstChar+3),d).decode("utf-8")+soaString(size,d,firstChar+2) 
    elif(d[firstChar]=='0' and  d[firstChar+1]=='0'):
         return ''
    else:
         return soaString(size,d,firstChar+2)
            
#HEX STR CHAR NUMBER-> int
def intmm(numstr):
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

def intm(st):
    if(st=='a'):
        return 10
    elif(st=='b'):
        return 11
    elif(st=='c'):
        return 12
    elif(st=='d'):
        return 13
    elif(st=='e'):
        return 14
    elif(st=='f'):
        return 15
    else:
        try:
            j=int( float(st) )
            return int(j)
        except TypeError:
            return -1

# OPT CODE
def oopt(numb):
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

#zERROR OR NO ERROR
def zzE(numb):
    if(numb==0):
        return "NO ERROR="+str(numb)
    else:
        return "ERROR="+str(numb)

# prints all header backwards data input


#copy from http
def doubleZero(d,location):
    if(intmm(d[location])==0 and intmm(d[location+1])==0):
        return location
    else:
        return doubleZero(d,location+1)

    #returns value of string of hex chars                                                           
def addHex(d,where,bytes):
    if(bytes<1):
        return intm(d[where])
    else:
        return intm(d[where])*16**bytes+addHex(d,where+1,bytes-1)

  #finds next location of 00 in hex string                                                       
def doubleZero(d,location):
    if(intm(d[location])==0 and intm(d[location+1])==0):
        return location
    else:
        return doubleZero(d,location+2)

 #deHexiflify recursive                                
def dehex(start,d):
    #print(d[start],d[start+1])
    if(intm(d[start])==12 or d[start]=='c'):
        j=intm(d[start+1])*(16**2)+intm(d[start+2])*(16**1)+intm(d[start+3])*(1)
        return dehex(j*2,d)
    count=intm(d[start])+intm(d[start+1])
    if(count>0):
        return bytearray.fromhex(d[start:(start+(count+1)*2)])+b'.'+dehex(start+count*2+2,d)
    else:
        return b''
 #deHexiflify recursive                                                                                                                                                                                  
def dehex3(start,d, end):
   # print(end, start)
    if(end==0):
        return''
    elif(start%2==0):
        end=end-1;
    #print(d[start],d[start+1])                                                                                                                                                                         
    if(intm(d[start])==12 or d[start]=='c'):
        j=intm(d[start+1])*(16**2)+intm(d[start+2])*(16**1)+intm(d[start+3])*(1)
        return dehex3(j*2,d,end)
    count=intm(d[start])+intm(d[start+1])
    if(count>0):
        return bytearray.fromhex(d[start:(start+(count+1)*2)])+b'.'+dehex3(start+count*2+2,d,end)
    else:
        return b''

#IP TO HEX CONVERSION                                                           
def ipToHex(d):
    #print (d.split('.'))                                                      
    t=d.split('.')
    return '0'+str(len(t[0]))+sInt2h(t[0]) +'0'+str(len(t[1]))+sInt2h(t[1])+'0'+str(len(t[2]))+sInt2h(t[2])+'0'+str(len(t[3]))+sInt2h(t[3])

def hostToHex(h):
    t=h.split('.')
    at=h.find('.')
    if(at>0):
        return '0'+str(len(t[0]))+s2h(t[0])+hostToHex(h[at+1:])
    else:
        return  '0'+str(len(t[0]))+s2h(t[0])

#gets the int value from type!
def intToType(t):
            return {
         1: "A",
         2: "NS",
         5: "CNAME",
         6: "SOA",
         11: "WKS",
         12: "PTR",
         13: "HINFO",
         14: "MINFO",
         15: "MX",
         16: "TXT",
         255: "ANY"
    }.get(t, "ANY")

def typeToInt(t):
    if(t=="A"):
        return 1
    elif(t=="NS"):
        return 2
    elif(t=="CNAME"):
        return 5
    elif(t=="SOA"):
        return 6
    elif(t=="WKS"):
        return 11
    elif(t=="PTR"):
        return 12
    elif(t=="HINFO"):
        return 13
    elif(t=="MINFO"):
        return 14
    elif(t=="MX"):
        return 15
    elif(t=="TXT"):
        return 16
    elif(t=="ANY"):
        return 255
    else:
        return 0
#string int 2 hex                                                                                                              
def sInt2h(s):
    if(len(s)>1):
        return format(ord(s[0]))+sInt2h(s[1:])
    else:
        return format(ord(s))

    #string 2 hex recursive through                                                          
def s2h(s):
    if(len(s)>0):
        b=s[0]
        return   format(ord(b),'x')+ s2h(s[1:])
    else:
        return 
