It is technically possible that my proctocol returns a return address
I Believe it would be more practical to have a return message at the 
implementation level. Although it could be possible to "DISSECT" the protocol
So the format is more like a handshake process.  

ORIGIN:                      DESTINATION:
MESSAGE to 999->
			     <-RECIEVED 999:
			     <-Command succesful/unsuccesful list
REPLY MESSAGE to 99->
			     <-RECIEVED 999: 
			     ALL SUCCESFUL (Hopefully)			     

 		 OOOOOORRRRRR

ORIGIN:                      DESTINATION:
MESSAGE to 999->
			    <- RECIEVED 999
			    <- CONFIRMATION ON PROCESS ONE REACHED AND EFFECTED
			    <- CONFIRMATION ON PROCESS TWO REACHED AND EFFECTED
			    <- CONFIRMATION ON PROCESS .... ETC
