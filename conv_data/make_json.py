import csv
import json
import os

# working directory is ./conv_data
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
            north_mesh = rel_array[i-1][j]
            if north_mesh == rel_array[-1][j]:
                north_mesh = None
            try:
                south_mesh = rel_array[i+1][j]
            except:
                south_mesh = None
            west_mesh = rel_array[i][j-1]
            if west_mesh == rel_array[i][-1]:
                west_mesh = None
            try:
                east_mesh = rel_array[i][j+1]
            except:
                east_mesh = None

            relation_array.append([
                base_mesh,
                north_mesh,
                south_mesh,
                west_mesh,
                east_mesh
            ])

with open(csv_info_path, 'r') as info_csv:
    info_reader = csv.reader(info_csv)
    info_array = [i for i in info_reader]
    mesh_list = [int(info_array[i][0]) for i in range(len(info_array))]
    lat_list = [float(info_array[i][1]) for i in range(len(info_array))]
    lng_list = [float(info_array[i][2]) for i in range(len(info_array))]
    mesh_items_num = len(mesh_list)

mesh_array = []
for i in range(mesh_items_num):
    mesh_dict = {
        "meshcode": mesh_list[i],
        "latitude": lat_list[i],
        "logitude": lng_list[i],
        "relation": {
            "north": relation_array[i][1],
            "south": relation_array[i][2],
            "west": relation_array[i][3],
            "east": relation_array[i][4]
        }
    }
    mesh_array.append(mesh_dict)
    # json_body["Node"][str(mesh_list[i])] = mesh_dict

json_body = {
    "Node":mesh_array
}

with open(pwd + '/mesh.json', 'w') as f:
    json.dump(json_body, f, indent=4, ensure_ascii=False)


