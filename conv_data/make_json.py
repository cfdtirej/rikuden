import csv
import json
import os

pwd = os.getcwd()
print(pwd)

csv_rel_path = pwd + '/mesh_rel.csv'
csv_info_path = pwd + '/mesh_info.csv'

with open(csv_rel_path, 'r') as rel_csv:
    rel_reader = csv.reader(rel_csv)
    rel_array = [i for i in rel_reader] # [[],[]]
    nones = lambda n: [None for _ in range(n)]
    up, down, left, right = nones(4)

    relation_array = []
    for i in range(len(rel_array)): # range(38)
        for j in range(len(rel_array[0])): # range(12)
            base_mesh = rel_array[i][j]
            # relation meshcode
            up_mesh = rel_array[i-1][j]
            if up_mesh == rel_array[-1][j]:
                up_mesh = None
            try:
                down_mesh = rel_array[i+1][j]
            except:
                down_mesh = None
            left_mesh = rel_array[i][j-1]
            if left_mesh == rel_array[i][-1]:
                left_mesh = None
            try:
                right_mesh = rel_array[i][j+1]
            except:
                right_mesh = None

            relation_array.append([
                base_mesh,
                up_mesh,
                down_mesh,
                left_mesh,
                right_mesh
            ])

with open(csv_info_path, 'r') as info_csv:
    info_reader = csv.reader(info_csv)
    info_array = [i for i in info_reader]
    mesh_list = [int(info_array[i][0]) for i in range(len(info_array))]
    lat_list = [float(info_array[i][1]) for i in range(len(info_array))]
    lng_list = [float(info_array[i][2]) for i in range(len(info_array))]
    mesh_items_num = len(mesh_list)

mesh_array = []
for meshcode, latitude, longitude, relations in zip(mesh_list, lat_list, lng_list, relation_array):
    for i in range(mesh_items_num):
        mesh_dict = {
            "meshcode": meshcode,
            "latitude": latitude,
            "logitude": longitude,
            "relation": {
                "up": relation_array[i][1],
                "down": relation_array[i][2],
                "left": relation_array[i][3],
                "right": relation_array[i][4]
            }
        }
        mesh_array.append(mesh_dict)

json_body = {"Node":mesh_array}
# with open('mesh_node_relation.json', 'w') as j:
#     json.dump(json_body, j)


