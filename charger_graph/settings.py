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
    'name': None,
    'meshcode': None,
    'latitude': None,
    'longitude': None,
    'time': None,
    'latest_used': None,
    'latest_stored': None,
    'after_30min': None,
    'after_60min': None,
    'after_90min': None,
    'after_120min': None,
    'after_150min': None,
    'after_180min': None,
    'north': None,
    'south': None,
    'west': None,
    'east': None,
    'ns_length': None,
    'we_length': None
}
