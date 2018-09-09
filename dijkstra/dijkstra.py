#nodes in order alphabetic
import sys
used=""
print("Give all the letters designating nodes start with y end with z abc... in the middle")
star= sys.stdin.readline()
#star='yabcdefz'
def getLetter(strg,used,dist):
    notdone=True
    it=0
    while(notdone):
        if(strg[it] not in used):
            if(dist[it]!=99):
                return strg[it]
        it+=1
    return it-1
arr=[[]]
dist=[]
def setDist(dist):
    for x in star[:len(star)-1]:
        if(x=='y'):
            dist.append(0)
        else:
            dist.append(99)
    print(dist)
setDist(dist)
print("enter all node connections ;(")
def getArray(star, arr):
    temp=0
    for x in star[:len(star)-1]:
        for y in star[:len(star)-1]:
            print( star[temp],"->",y)
            data = int(input())
            arr[temp].append(data)
        arr.append([])
        temp+=1;
getArray(star,arr)
print("array:",arr)
print("nodes:",star)
     #y a b c d e f z
"""arr=[[0,3,2,5,0,0,0,0],
     [3,0,0,0,3,0,0,0],
     [2,0,0,0,1,6,0,0],
     [5,0,0,0,0,2,0,0],
     [0,3,1,0,0,0,4,0],
     [0,0,6,2,0,0,1,4],
     [0,0,0,0,4,1,0,2],
     [0,0,0,0,0,4,2,0]] """

#dist=[0,99,99,99,99,99,99,99]
pushed=0
temp=0;
shortest=99;
got=True;
for x in star[:len(star)-2]:
    print("start of Loop:",star,"letter:",star[pushed],"pushed:",pushed)
    print(arr[pushed])
    print(used)
    currentLetter=star[pushed]
    shortest=99
    temp=0
    for y in arr[pushed]:
        #print(" Y:",y," ",end='')
        if(y!=0): # if non zero site
            if(dist[temp]>y+dist[pushed]):
                dist[temp]=y+dist[pushed]# new dist value
                #print(start[pushed],dist[y])                    
        temp+=1;
    used=used+currentLetter
    shortest=star.find(getLetter(star,used,dist) )
    #print()
    """if(shortest>10):
        i=0
        for k in start:
            i+=1
            if(k  not in used): """
                
    pushed=shortest
    print(dist,":DIST")
