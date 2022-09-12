host="192.168.43.79"            # Set the server address to variable host
import time
port=4446               # Sets the variable port to 4446
time.sleep(5)
from multiprocessing.reduction import recv_handle
from socket import *             # Imports socket module

s=socket(AF_INET, SOCK_STREAM)      # Creates a socket
s.connect((host,port))

def my_recv(msg_length):
    chunks = []
    bytes_to_recv = msg_length
    while bytes_to_recv:
        chunk = s.recv(bytes_to_recv)
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_to_recv -= len(chunk)
    return b''.join(chunks)

i = 0
while True:
    image_length_bytes = my_recv(4)
    image_length = int.from_bytes(image_length_bytes, 'big')
    with open(str(i) + "s.jpg", "wb") as f:
        bytes_to_recv = image_length
        while bytes_to_recv:
            recv_data = my_recv(min(4096, bytes_to_recv))
            f.write(recv_data)
            bytes_to_recv -= len(recv_data)

    i += 1
