from py2neo import Graph, Node, Relationship, NodeMatcher
from py2neo.ogm import GraphObject
from neo4j import GraphDatabase

import mesh_info


HOST = 'localhsot:7687'
AUTH = ('neo4j', 'password')

node_num = mesh_info.node_num
mesh = mesh_info.mesh_list
latitude = mesh_info.latitude_list
longitude = mesh_info.longitude_list
relation_dict = mesh_info.relation_dict_list

query = '''
MATCH (main_node:Mesh {meshcode:$main_mesh),
      (to_node:Mesh {meshcode:$to_mesh})
MERGE (main_node)-[:LENGTH {length:$length}->(to_node)
MERGE (main_node)<-[:LENGTH {length:$length}-(to_node)
'''


def create_mesh_node():

    graphdb = Graph(HOST,auth=AUTH)
    for i in range(node_num):
        node = Node('Mesh')
        node['name'] = 'Mesh_' + str(mesh[i])
        node['meshcode'] = mesh[i]
        node['latitude'] = latitude[i]
        node['longitude'] = longitude[i]
        graphdb.merge(node, 'Mesh', 'name')

    for i in range(node_num):
        driver = GraphDatabase.driver(HOST, auth=AUTH, encrypted=False)

        def node_association(tx, main_mesh, to_mesh, length):
            tx.run(query, main_mesh=main_mesh, to_mesh=to_mesh, length=length)

        with driver.session() as session:
            session.write_transaction(node_association)



create_mesh_node()

