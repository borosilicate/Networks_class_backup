import socket   #necesary for hw
import _thread  #for concurrency
import random   #random joke
import sys      #argument 

#variable for quantitiy of arguments
arguments=len(sys.argv)

connection= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
connection.bind(("0.0.0.0",47645))
connection.listen(10) #ten people

#To help speed up grading this tells the telnet to connect to 
print("\n\t\tcommand to connect: telnet ", socket.getfqdn() , connection.getsockname()[1],"\n ")
print("Special thanks to Sarah @  frugalfun4boys.com for providing all the jokes on this server! \n")
print("\t https://frugalfun4boys.com/2016/05/11/knock-knock-jokes-for-kids/ \t \n")

nouns=[] 
nouns.append("GOLIATH");     nouns.append("BROCCOLI");
nouns.append("WOODEN SHOE"); nouns.append("AMISH.");
nouns.append("BOO.");        nouns.append("ATCH.");
nouns.append("HARRY.");      nouns.append("CASH.");
nouns.append("BIG. INTERRUPTING COW."); nouns.append("CANOE.");
nouns.append(" Lettuce.");   nouns.append("  I am.  ");
nouns.append("Ice cream.");  nouns.append(" Doctor. ");
nouns.append("Yah. ");       nouns.append(" Nana.");
nouns.append(" Justin");     nouns.append(" Alpaca.");
nouns.append("Tank.");       nouns.append("Car go.");
nouns.append(" Leaf.");      nouns.append(" Isabel.");
nouns.append("Dishes."); 
joke=[]
joke.append("GOLIATH DOWN, YOU LOOK-ETH TIRED!") 
joke.append("BROCCOLI DOESN'T HAVE A LAST NAME, SILLY.")
joke.append("WOODEN SHOE LIKE TO HEAR ANOTHER JOKE")
joke.append("AMISH WHO? REALLY? YOU DON'T LOOK LIKE A SHOE!")
joke.append("WHY ARE YOU CRYING?") 
joke.append("BLESS YOU!")
joke.append("HARRY UP AND ANSWER THE DOOR!")
joke.append("NO THANKS BUT I'LL TAKE A PEANUT IF YOU HAVE ONE!")
joke.append("MOOOOOOOO!") 
joke.append("CANOE COME OUT AND PLAY WITH ME?")
joke.append("Lettuce in, it’s cold out here!")
joke.append("You don’t know who you are?")
joke.append("Ice cream if you don’t let me in!")
joke.append(" You’ve seen that TV show?")
joke.append(" No, I prefer google.")
joke.append(" Nana your business!")
joke.append("Justin the neighborhood and thought I’d come over!")
joke.append("Alpaca the suitcase, you load the car!")
joke.append("You’re welcome!")
joke.append("Car go BEEP BEEP!")
joke.append(" Leaf me alone!")
joke.append(" Isabel working? I had to knock!")
joke.append(" Dishes the police! Open up!")

#Method/Function Calls joke on Client
def userJoke(client, adress):
   #""" creating the  object for knock knock and who's there"""
   knock="KNOCK KNOCK\n"
   kk = knock.encode('utf-8')
   who="WHO'S THERE?\r\n"
   w=who.encode('utf-8')

#This one has no concurrency
#if statment check to see if there is another arg
   while True:
      randomNumber=random.randint(0,22)
       #print(client) could send somewhere to keep track of who is connecting ;D 
      data=kk
      #Only goes when they send WHO'S THERE?\n\r
      while data!=(w):
         randomNumber=random.randint(0,22);
         #knock="KNOCK KNOCK \r\n"
         #kk2 = knock.encode('utf-8')
         client.send(kk);
         data =client.recv(47645);
         # print('received {} of length {}'.format(data, len(data)))
      # send joke response based on them answering from arrays above
      # It will be after who's there?
      randomJokeString=(nouns[randomNumber]+"\n").upper()
      #Transoforms string to bits
      encodedRJS=randomJokeString.encode('utf-8')
      #sends to client
      client.send(encodedRJS)
      #Waits for response
      data2=client.recv(47645)
      #then encodes next part and sends
      randomJokeString2=(joke[randomNumber]+"\n").upper();
      encodedRJS2=randomJokeString2.encode('utf-8');
      client.send(encodedRJS2);
      #then disconnects
      client.shutdown(socket.SHUT_RDWR)
      client.close()

if(arguments==2):
   while True:
      client , adress = connection.accept() #connect person
      userJoke(client,adress)
      
else:
#attempt at Concurrency
   print("\t  A WILD CONCURRENCY ATTEMPT APPEARED!!! CONCURRENCY??? \n ")
   while True:
      client, adress = connection.accept();
      _thread.start_new_thread(userJoke,(client,adress))
   connection.close()
#TRYMOVING AROUND LAST LINE
