from socket import *

serverPort = 6789

welcomeSocket = socket()
welcomeSocket.bind (('',serverPort))

welcomeSocket.listen(2)
print ("SERVER LISTENING")

while True:
    connectionSocket, addr = welcomeSocket.accept()
    print(addr)
    inStream = connectionSocket.makefile("r")
    outStream = connectionSocket.makefile("w") 
    
    clientSentence = inStream.readline()
    capitalizedSentence = clientSentence.upper()
    outStream.writelines(capitalizedSentence+"\n")
    outStream.flush()
    connectionSocket.close()