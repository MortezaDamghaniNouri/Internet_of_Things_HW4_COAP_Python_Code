import socket

homeData = []
farmData = []


localIP = "192.168.1.101"
localPort = 20001
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("COAP server up and listening")
# Listening for incoming clients
while True:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientIP = "Client IP Address:{}".format(address)
    clientMessage = str(message.decode())
    print(clientMessage)
    print(clientIP)
    if clientMessage.find("put") != -1:
        i = 0
        while i < 10:
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0]
            clientMessage = str(message.decode())
            print("Client message: " + clientMessage)
            if clientMessage.find("Home") != -1:
                j = clientMessage.find("payload") + 9
                input_data = ""
                clientMessageList = list(clientMessage)
                while j < len(clientMessageList):
                    input_data += clientMessageList[j]
                    j += 1
                homeData.append(input_data)

            if clientMessage.find("Farm") != -1:
                j = clientMessage.find("payload") + 9
                input_data = ""
                clientMessageList = list(clientMessage)
                while j < len(clientMessageList):
                    input_data += clientMessageList[j]
                    j += 1
                farmData.append(input_data)
            i += 1

    if clientMessage.find("get") != -1 and clientMessage.find("home") != -1:
        i = 0
        while i < 10:
            msgFromServer = homeData[i]

            bytesToSend = str(msgFromServer).encode()

            UDPServerSocket.sendto(bytesToSend, address)
            i += 1
    if clientMessage.find("get") != -1 and clientMessage.find("farm") != -1:
        i = 0
        while i < 10:
            msgFromServer = farmData[i]

            bytesToSend = str(msgFromServer).encode()

            UDPServerSocket.sendto(bytesToSend, address)
            i += 1


    # Sending final response to the clients
    msgFromServer = "version: 1, type: NON, code: put, payload: Done"
    bytesToSend = str.encode(msgFromServer)
    UDPServerSocket.sendto(bytesToSend, address)

    # print("Farm: ")
    # for i in farmData:
    #     print(i)
    # print("Home: ")
    # for i in homeData:
    #     print(i)

