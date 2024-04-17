# socket_echo_server_dgram.py

from socket import *

serverPort = 6789
# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', serverPort)
print('starting up on {} port {}'.format(*server_address))
serverSocket.bind(server_address)

while True:
    print('\nwaiting to receive message')
    # Receive from [buffer_size]
    data, address = serverSocket.recvfrom(4096)
    print('received {} bytes from {}'.format(len(data), address))
    print(str(data))
    if data:
        # Trasforma in stringa utf-8 -> maiuscolizza quest'ultima -> ritrasforma in byte array -> invia quest'ultimo
        sent = serverSocket.sendto(data.decode().upper().encode(), address)

        print('sent {} bytes back to {}'.format(sent, address))