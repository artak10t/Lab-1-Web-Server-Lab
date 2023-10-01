#import socket module
from socket import *
import sys

#Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 6789))
serverSocket.listen(1)

while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept() #Fill in start #Fill in end
    try:
        message = connectionSocket.recv(1024) #Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read() #Fill in start #Fill in end

        #Send one HTTP header line into socket
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n'.encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("\nHTTP/1.1 404 Not Found\n\n".encode())
        
        #Close client socket
        connectionSocket.close()

serverSocket.close()
sys.exit() #Terminate the program after sending the corresponding data 