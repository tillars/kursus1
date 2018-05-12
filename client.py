import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))

while (True):
    inp = input ("Indskriv tekst som skal sendes : ")
    clientsocket.sendall(inp.encode("utf-8"))