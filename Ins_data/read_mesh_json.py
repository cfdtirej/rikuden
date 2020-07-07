import json
import os
import pprint

pwd = os.getcwd()
path = pwd + '/Ins_data/mesh.json'

# mesh.json
with open(path, 'r', encoding='utf-8') as f:
    json_body = json.load(f)
    node_num = len(json_body['Node'])
    mesh_list = [json_body['Node'][i]['meshcode'] for i in range(node_num)]
    latitude_list = [json_body['Node'][i]['latitude'] for i in range(node_num)]
    longitude_list = [json_body['Node'][i]['longitude'] for i in range(node_num)]
    relation_dict_list = [json_body['Node'][i]['relation'] for i in range(node_num)]
'''memo
north, south : 463m
west, east : 559m
'''
