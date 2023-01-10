import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = '127.0.0.1'
server_port = 65432

server = (server_address, server_port)
sock.bind(server)
print("Listening on " + server_address + ":" + str(server_port))

while True:
    payload, client_address = sock.recvfrom(1024)
    print("Echoing message back to " + str(client_address))
    print(payload)
    sent = sock.sendto(payload, client_address)
    print(sent)