from socket import *

serverIP = '172.17.96.1'
serverPort = 6789

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverIP,serverPort))

sentence = input('Frase in minuscolo:')
outStream = clientSocket.makefile("w")
inStream = clientSocket.makefile("r")

outStream.writelines(sentence+"\n")
outStream.flush()
modifiedSentence = inStream.readline()
print("FROM SERVER: ", modifiedSentence)

clientSocket.close()