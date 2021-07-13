import socket

homeData = []
farmData = []



localIP = "192.168.1.101"

localPort = 20001

bufferSize = 1024



# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))

print("COAP server up and listening")

# Listening for incoming clients

while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMethod = str(message.decode())
    clientIP = "Client IP Address:{}".format(address)

    print(clientMethod)
    print(clientIP)


    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    clientPayloadSize = str(message.decode())
    print("Client payload size consists of " + clientPayloadSize + " parts")

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    clientFunctionality = str(message.decode())
    print("Client functionality: " + clientFunctionality)


    if clientMethod == "put" and clientFunctionality == "home":
        i = 0
        while i < int(clientPayloadSize):
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

            message = bytesAddressPair[0]

            clientMessage = str(message.decode())
            print("Client message: " + clientMessage)
            homeData.append(clientMessage)
            i += 1

    if clientMethod == "put" and clientFunctionality == "farm":
        i = 0
        while i < int(clientPayloadSize):
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

            message = bytesAddressPair[0]

            clientMessage = str(message.decode())
            print("Client message: " + clientMessage)
            farmData.append(clientMessage)
            i += 1

    if clientMethod == "get" and clientFunctionality == "home":
        i = 0
        while i < int(clientPayloadSize):
            msgFromServer = homeData[i]

            bytesToSend = str.encode(msgFromServer)

            UDPServerSocket.sendto(bytesToSend, address)
            i += 1

    if clientMethod == "get" and clientFunctionality == "farm":
        i = 0
        while i < int(clientPayloadSize):
            msgFromServer = farmData[i]

            bytesToSend = str.encode(msgFromServer)

            UDPServerSocket.sendto(bytesToSend, address)
            i += 1

    print("THE FARM DATA IS: ")
    for i in farmData:
        print(i)

    print("THE HOME DATA IS: ")
    for i in homeData:
        print(i)

    # Sending a reply to client
    msgFromServer = "Done"
    bytesToSend = str.encode(msgFromServer)
    UDPServerSocket.sendto(bytesToSend, address)