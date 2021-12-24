import socket

serversocket = socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)

host = socket.gethostname()
port = 444

serversocket.bind(
    ("192.168.29.43",
    port)
)


serversocket.listen(
    2
)

print("Connection Requirements Complete")


while True:
    clientsocket, address = serversocket.accept()
    
    print(
        "Connection Established to", str(address)
    )

    message = "Hello! You have successfully connected to the server" + "\r\n"

    clientsocket.send(
        message.encode(
            'ascii'
        )
    )

    clientsocket.close()
