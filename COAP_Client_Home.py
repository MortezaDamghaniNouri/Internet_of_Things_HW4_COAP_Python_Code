import socket

data = [
{"ID": "Home1", "Parking": "Full", "Energy Consumption(Watt)": 10, "Lights": "off", "Temperature": 23, "Doors": "Locked"},
{"ID": "Home2", "Parking": "Empty", "Energy Consumption(Watt)": 12, "Lights": "off", "Temperature": 50, "Doors": "Unlocked"},
{"ID": "Home3", "Parking": "Full", "Energy Consumption(Watt)": 1200, "Lights": "on", "Temperature": 32, "Doors": "Unlocked"},
{"ID": "Home4", "Parking": "Full", "Energy Consumption(Watt)": 2000, "Lights": "on", "Temperature": 67, "Doors": "Unlocked"},
{"ID": "Home5", "Parking": "Empty", "Energy Consumption(Watt)": 3000, "Lights": "on", "Temperature": 76, "Doors": "Unlocked"},
{"ID": "Home6", "Parking": "Empty", "Energy Consumption(Watt)": 4500, "Lights": "on", "Temperature": 55, "Doors": "Locked"},
{"ID": "Home7", "Parking": "Empty", "Energy Consumption(Watt)": 1800, "Lights": "off", "Temperature": 45, "Doors": "Locked"},
{"ID": "Home8", "Parking": "Full", "Energy Consumption(Watt)": 10000, "Lights": "on", "Temperature": 20, "Doors": "Unlocked"},
{"ID": "Home9", "Parking": "Full", "Energy Consumption(Watt)": 2220, "Lights": "off", "Temperature": 15, "Doors": "Locked"},
{"ID": "Home10", "Parking": "Empty", "Energy Consumption(Watt)": 3000, "Lights": "off", "Temperature": 12, "Doors": "Unlocked"},
]

serverAddressPort = ("192.168.1.101", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
coap_packet = "version: 1, type: NON, code: put, payload: start_communication"
bytesToSend = str.encode(coap_packet)
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
i = 0
while i < 10:

    string_data = str(data[i])
    coap_packet = "version: 1, type: NON, code: put, payload: " + string_data
    bytesToSend = str.encode(coap_packet)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    i += 1



msgFromServer = UDPClientSocket.recvfrom(bufferSize)
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)