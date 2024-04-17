# socket_echo_client_dgram.py

from socket import *
from time import sleep

serverName = '127.0.0.1'
serverPort = 6789

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
server_address = (serverName, serverPort)

sentence = input('Frase in minuscolo:')

try:
    # Send data
    print('sending {!r}'.format(sentence))
    sent = clientSocket.sendto(sentence.encode('utf-8'), server_address)

    # Receive response
    print('waiting to receive')
    data, server = clientSocket.recvfrom(4096)
    print('received {!r}'.format(data))

finally:
    sleep(10)
    print('closing socket')
    clientSocket.close()