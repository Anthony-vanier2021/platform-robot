import socket

Dest_IP = '192.168.53.4' # Get IP from serial connection
Dest_Port = 2001                    #server port
Destination = (Dest_IP,Dest_Port)   #server full address including port
UDPclient = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #Opening socket

ClientMsg = input("Please Enter Message to ESP32: ")
Msg2Server = str.encode(ClientMsg)      #encode message for network communication
UDPclient.sendto(Msg2Server,Destination)    #send message to server
print(f"Sending {ClientMsg} to ESP32")
if ClientMsg == "END":
    print("Goodbye!")
    UDPclient.close()   #closing socket
