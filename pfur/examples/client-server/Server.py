import socket

# create socket
my_amazing_server_socket = socket.socket()

# configure host and port
host = 'localhost'
port = 8888
my_amazing_server_socket.bind((host, port))

# configure max connections count and start listening port
my_amazing_server_socket.listen(3)
# accept connection from addres
connection, address = my_amazing_server_socket.accept()
while True:
    # decode received bytes to utf-8
    user_message = connection.recv(16384).decode()
    print("Client message: " + user_message)
    # send response back
    connection.send(b"Got you message: " + user_message.encode("utf-8"))