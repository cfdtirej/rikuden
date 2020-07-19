import json


with open('mesh.json', 'r', encoding='utf-8') as f:
    mesh_json = json.load(f)
    charger = mesh_json["Node"]

HOST = 'bolt://localhost:7687'
AUTH = ('neo4j', 'password')
API_URL = 'http://localhost:5000/charger'

charger1 = [i for i in charger if i["meshcode"] == 543761952][0]
charger2 = [i for i in charger if i["meshcode"] == 543761793][0]
charger3 = [i for i in charger if i["meshcode"] == 543761063][0]
charger4 = [i for i in charger if i["meshcode"] == 543761283][0]

charger1_json= {
    'node_label': "Charger",
    'meshcode': charger1["meshcode"],
    'latitude': charger1["latitude"],
    'longitude': charger1["longitude"],
    'north': charger1['relation']['north'],
    'south': charger1['relation']['south'],
    'west': charger1['relation']['west'],
    'east': charger1['relation']['east'],
    'ns_length': 463,
    'we_length': 559
}

charger2_json = {
    'node_label': 'Charger',
    'meshcode': charger2["meshcode"],
    'latitude': charger2["latitude"],
    'longitude': charger2["longitude"],
    'north': charger2['relation']['north'],
    'south': charger2['relation']['south'],
    'west': charger2['relation']['west'],
    'east': charger2['relation']['east'],
    'ns_length': 463,
    'we_length': 559
}

charger3_json = {
    'node_label': 'Charger',
    'meshcode': charger3["meshcode"],
    'latitude': charger3["latitude"],
    'longitude': charger3["longitude"],
    'north': charger3['relation']['north'],
    'south': charger3['relation']['south'],
    'west': charger3['relation']['west'],
    'east': charger3['relation']['east'],
    'ns_length': 463,
    'we_length': 559
}

charger4_json = {
    'node_label': 'Charger',
    'meshcode': charger4["meshcode"],
    'latitude': charger4["latitude"],
    'longitude': charger4["longitude"],
    'north': charger4['relation']['north'],
    'south': charger4['relation']['south'],
    'west': charger4['relation']['west'],
    'east': charger4['relation']['east'],
    'ns_length': 463,
    'we_length': 559
}

