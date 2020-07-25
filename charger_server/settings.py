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

