host="192.168.43.79"                # Set the server address to variable host
port=4446                   # Sets the variable port to 4446
import os
import time
from socket import *
import win32
import pyautogui
import mss
s=socket(AF_INET, SOCK_STREAM)

s.bind((host,port))
s.listen(1) # This should be called

print("Listening for connections.. ")
q,addr=s.accept()
print("Connected to: " + str(addr))
frames = int(input("enter number of frames: "))
i = 0


with mss.mss() as mss_instance:
    while True:

        mss_instance.shot(output=str(i) + ".jpg")
        with open(str(i) + ".jpg", "rb") as f:
            # Get length by positioning to end of file
            image_length = f.seek(0, 2)
            f.seek(0, 0) # Seek back to beginning of file
            # Convert image length to a 4-byte array:
            image_length_bytes = image_length.to_bytes(4, 'big')
            q.sendall(image_length_bytes)
            data = f.read(4096)
            while len(data):
                q.sendall(data)
                data = f.read(4096)
        time.sleep(1/frames)
        i += 1
