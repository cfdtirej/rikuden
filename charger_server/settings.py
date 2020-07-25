import json


with open('mesh.json', 'r', encoding='utf-8') as f:
    mesh_json = json.load(f)
    charger = mesh_json["Node"]

HOST = 'bolt://localhost:7687'
AUTH = ('neo4j', 'password')

charger1 = [i for i in charger if i["meshcode"] == 543761952][0]
charger2 = [i for i in charger if i["meshcode"] == 543761793][0]
charger3 = [i for i in charger if i["meshcode"] == 543761063][0]
charger4 = [i for i in charger if i["meshcode"] == 543761283][0]

graph_json = {
    'ns_length': 463,
    'we_length': 559,
}

c1_info = {
    'Label': 'Charger1',
    'north': charger1['relation']['north'],
    'south': charger1['relation']['south'],
    'west': charger1['relation']['west'],
    'east': charger1['relation']['east'],
    'meshcode': charger1['meshcode'],
    'latitude': charger1['latitude'],
    'longitude': charger1['longitude'],
    'ns_length': 463,
    'we_length': 559
}

c2_info = {
    'Label': 'Charger2',
    'north': charger2['relation']['north'],
    'south': charger2['relation']['south'],
    'west': charger2['relation']['west'],
    'east': charger2['relation']['east'],
    'meshcode': charger2['meshcode'],
    'latitude': charger2['latitude'],
    'longitude': charger2['longitude'],
    'ns_length': 463,
    'we_length': 559
}

c3_info = {
    'Label': 'Charger3',
    'north': charger3['relation']['north'],
    'south': charger3['relation']['south'],
    'west': charger3['relation']['west'],
    'east': charger3['relation']['east'],
    'meshcode': charger3['meshcode'],
    'latitude': charger3['latitude'],
    'longitude': charger3['longitude'],
    'ns_length': 463,
    'we_length': 559
}

c4_info = {
    'Label': 'Charger4',
    'north': charger4['relation']['north'],
    'south': charger4['relation']['south'],
    'west': charger4['relation']['west'],
    'east': charger4['relation']['east'],
    'meshcode': charger4['meshcode'],
    'latitude': charger4['latitude'],
    'longitude': charger4['longitude'],
    'ns_length': 463,
    'we_length': 559
}

