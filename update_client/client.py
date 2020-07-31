import csv
import json
import socket
import time
import random
import pprint


HOST = 'localhost'
PORT = 50002

with open('./sample.csv', 'r') as f:
    reader = csv.reader(f)
    table = [i for i in reader]
    field = table[1:]
count = 0
while True:
    current_time = int(time.time())
    if current_time % 30 == 0:
        print(count)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            json_body = {
                "CHARGER":
                    [
                        {
                            'name': 'charger1',
                            'time': int(field[count][0]),
                            'used_latest': int(field[count][1]),
                            'stored_latest': int(field[count][2]),
                            "used_after_030": int(field[count][3]),
                            "used_after_060": int(field[count][4]),
                            "used_after_090": int(field[count][5]),
                            "used_after_120": int(field[count][6]),
                            "used_after_150": int(field[count][7]),
                            "used_after_180": int(field[count][8]),
                            "stored_after_030": int(field[count][9]),
                            "stored_after_060": int(field[count][10]),
                            "stored_after_090": int(field[count][11]),
                            "stored_after_120": int(field[count][12]),
                            "stored_after_150": int(field[count][13]),
                            "stored_after_180": int(field[count][14])
                        },
                        {
                            'name': 'charger2',
                            'time': int(field[count][0]),
                            'used_latest': int(field[count][1]),
                            'stored_latest': int(field[count][2]),
                            "used_after_030": int(field[count][3]),
                            "used_after_060": int(field[count][4]),
                            "used_after_090": int(field[count][5]),
                            "used_after_120": int(field[count][6]),
                            "used_after_150": int(field[count][7]),
                            "used_after_180": int(field[count][8]),
                            "stored_after_030": int(field[count][9]),
                            "stored_after_060": int(field[count][10]),
                            "stored_after_090": int(field[count][11]),
                            "stored_after_120": int(field[count][12]),
                            "stored_after_150": int(field[count][13]),
                            "stored_after_180": int(field[count][14])
                        },
                        {
                            'name': 'charger3',
                            'time': int(field[count][0]),
                            'used_latest': int(field[count][1]),
                            'stored_latest': int(field[count][2]),
                            "used_after_030": int(field[count][3]),
                            "used_after_060": int(field[count][4]),
                            "used_after_090": int(field[count][5]),
                            "used_after_120": int(field[count][6]),
                            "used_after_150": int(field[count][7]),
                            "used_after_180": int(field[count][8]),
                            "stored_after_030": int(field[count][9]),
                            "stored_after_060": int(field[count][10]),
                            "stored_after_090": int(field[count][11]),
                            "stored_after_120": int(field[count][12]),
                            "stored_after_150": int(field[count][13]),
                            "stored_after_180": int(field[count][14])
                        },
                        {
                            'name': 'charger4',
                            'time': int(field[count][0]),
                            'used_latest': int(field[count][1]),
                            'stored_latest': int(field[count][2]),
                            "used_after_030": int(field[count][3]),
                            "used_after_060": int(field[count][4]),
                            "used_after_090": int(field[count][5]),
                            "used_after_120": int(field[count][6]),
                            "used_after_150": int(field[count][7]),
                            "used_after_180": int(field[count][8]),
                            "stored_after_030": int(field[count][9]),
                            "stored_after_060": int(field[count][10]),
                            "stored_after_090": int(field[count][11]),
                            "stored_after_120": int(field[count][12]),
                            "stored_after_150": int(field[count][13]),
                            "stored_after_180": int(field[count][14])
                        },
                    ]
            }
            msg_json = json.dumps(json_body)
            s.connect((HOST, PORT))
            s.sendall(msg_json.encode('utf-8'))
            recv_msg = s.recv(1024)
            print(repr(recv_msg))
            print('-------------------')
            count += 1
            if count == 48:
                break
            time.sleep(20)

