import socket

my_little_client_socket = socket.socket()

# configure host and port
host = 'localhost'
port = 8888

# connect to host
my_little_client_socket.connect((host, port))

# send data
while True:
    data = input('Enter your input:')
    my_little_client_socket.send(data.encode())

    # listen response
    answer = my_little_client_socket.recv(16384)
    print(answer.decode("utf-8"))
