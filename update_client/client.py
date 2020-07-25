import json
import socket
import time
import random

import make_json


HOST = 'localhost'
PORT = 50002

while True:
    current_time = int(time.time())
    if current_time % 5 == 0:
        print(current_time)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            msg_json = make_json.make_json(current_time)
            msg_json = json.dumps(msg_json)
            s.connect((HOST, PORT))
            s.sendall(msg_json.encode('utf-8'))
            recv_msg = s.recv(1024)
            time.sleep(1)
            print(repr(recv_msg))