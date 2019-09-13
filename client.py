#SWDV-660 – Applied DevOps
#Maryville University, 2019
#Week 4 Assignment: Python Socket Client
#client.py
#Henrik Olsen (0913075)


import socket


#constants
HOST = '127.0.0.1'  # server's IP address (could have been a hostname)
PORT = 9500         # port number, as required per assignment


#function that print a "menu" and get user input
def getInput():
    print()
    print("Enter '0' (zero) to close client")
    print("Enter anything else and send that to the server")
    print()
    inputStr = input("Input> ")
    print()
    print()
    return inputStr


def main():
    #run infinite loop
    while True:
        clientInput = getInput()

        #break infinite loop if user requests it
        if clientInput == "0":
            break

        #create socket and open session
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((HOST, PORT))

        #send client input via connection/socket to server
        connection.send(clientInput.encode())

        #get response from server and print it out
        serverReply = connection.recv(1024).decode()
        print("Reply received from server: " + serverReply)


main()
