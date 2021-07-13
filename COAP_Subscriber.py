import socket

farm_file = open("E:\MyCodes\Web Codes\IoT_HW4_COAP_Subscriber\Farm_Content.txt", "wt")
farm_file.write("\n")
home_file = open("E:\MyCodes\Web Codes\IoT_HW4_COAP_Subscriber\Home_Content.txt", "wt")
home_file.write("\n")
farm_file.close()
home_file.close()
farm_file = open("E:\MyCodes\Web Codes\IoT_HW4_COAP_Subscriber\Farm_Content.txt", "at")
home_file = open("E:\MyCodes\Web Codes\IoT_HW4_COAP_Subscriber\Home_Content.txt", "at")


# Getting farm content
serverAddressPort = ("192.168.1.101", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
msgFromClient = "version: 1, type: NON, code: get, functionality: farm, payload: start_communication"
bytesToSend = str.encode(msgFromClient)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

i = 0
while i < 10:
    bytesAddressPair = UDPClientSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    serverMessage = str(message.decode())
    print("Server message: " + serverMessage)
    farm_file.write(serverMessage + "\n")
    i += 1
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)

# Getting home content
serverAddressPort = ("192.168.1.101", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
msgFromClient = "version: 1, type: NON, code: get, functionality: home, payload: start_communication"
bytesToSend = str.encode(msgFromClient)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
i = 0
while i < 10:
    bytesAddressPair = UDPClientSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    serverMessage = str(message.decode())
    print("Server message: " + serverMessage)
    home_file.write(serverMessage + "\n")
    i += 1
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)

farm_file.close()
home_file.close()



















