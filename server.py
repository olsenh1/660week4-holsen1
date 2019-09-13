#SWDV-660 – Applied DevOps
#Maryville University, 2019
#Week 4 Assignment: Python Socket Server
#server.py
#Henrik Olsen (0913075)


import socket


#constants
HOST = '127.0.0.1'  # server's IP address (could have been a hostname)
PORT = 9500         # port number, as required per assignment


def main():
    #create socket and bind it to host and port
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.bind((HOST, PORT))
    #start listening
    connection.listen()

    #loop - run until "shutdown-code" is received
    runServer = True
    while runServer:
        #create session
        session, addr = connection.accept()

        #get data (string) from client
        receivedData = session.recv(1024).decode()

        #create server output - default is "Goodbye"
        outputData = "Goodbye"
        #only if "Hello" is received, reply with "Hi"
        if receivedData == "Hello":
            outputData = "Hi"

        #send response to client
        session.send(outputData.encode())

        #close session
        session.close()


main()
