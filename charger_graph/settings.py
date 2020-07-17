import json

with open('mesh.json', 'r', encoding='utf-8') as f:
    mesh_json = json.load(f)
    charger = mesh_json["Node"]

charger1 = [i for i in charger if i["meshcode"] == 543761952][0]
charger2 = [i for i in charger if i["meshcode"] == 543761793][0]
charger3 = [i for i in charger if i["meshcode"] == 543761063][0]
charger4 = [i for i in charger if i["meshcode"] == 543761283][0]

HOST = 'bolt://localhost:7687'
AUTH = ('neo4j', 'password')

data_dict = {
    'node_label': 'Charger',
    'name': 'name',
    'meshcode': charger1['meshcode'],
    'latitude': ['latitude'],
    'longitude': charger1['longitude'],
    'time': 2020,
    'latest_used': 'latest_used',
    'latest_stored': 'latest_stored',
    'after_30min': 'after_30min',
    'after_60min': 'after_60m',
    'after_90min': 'after_90min',
    'after_120min': 'after_120min',
    'after_150min': 'after_150min',
    'after_180min': 'after_180min',
    'north': charger1['relation']['north'],
    'south': charger1['relation']['south'],
    'west': charger1['relation']['west'],
    'east': charger1['relation']['east'],
    'ns_length': 463,
    'we_length': 559
}
