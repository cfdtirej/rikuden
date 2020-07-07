from py2neo import Graph, Node, Relationship, NodeMatcher
from py2neo.ogm import GraphObject

import read_mesh_json

HOST = 'localhsot:7687'
AUTH = ('neo4j', 'password')

node_num = read_mesh_json.node_num
mesh = read_mesh_json.mesh_list
latitude = read_mesh_json.latitude_list
longitude = read_mesh_json.longitude_list
relation_dict = read_mesh_json.relation_dict_list


# def create_mesh_node():
#     graphdb = Graph(HOST,auth=AUTH)
#     for i in range(node_num):
#         node = Node('Mesh')
#         node['name'] = 'Mesh_' + str(mesh[i])
#         node['meshcode'] = mesh[i]
#         node['latitude'] = latitude[i]
#         node['longitude'] = longitude[i]
        # graphdb.create(node)
    # for i in range(node_num):
    #     main_node = Node

# create_mesh_node()

