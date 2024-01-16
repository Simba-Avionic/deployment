from utils.sender import Sender
import time
import logging

logging.basicConfig(level=logging.DEBUG)

def socketCallback(data,client_adress):
    print(data)
    print(client_adress)

s=Sender("test_tar.tar",socketCallback)
print("start sending file")
s.sendData()
time.sleep(2)