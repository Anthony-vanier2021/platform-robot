#Anthony Tremblay - Socket Programming
import socket, config

bufferSize = 1024
serverPort = 2001

try:
    UDPserver = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("Successful Socket Created")
except socket.error as error:
    print("ERROR: Socket error encountered: %s"%(error))

UDPserver.bind((config.IP_ADDRESS,serverPort))
print(f"Server ready @ {config.IP_ADDRESS}:{serverPort}")

while True:
    clientMsg, returnDest = UDPserver.recvfrom(bufferSize)
    data = clientMsg.decode() 
    returnIP = returnDest[0]
    print(data)
    if data == "END":
        break;

UDPserver.close()

