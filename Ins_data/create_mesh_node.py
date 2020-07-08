from py2neo import Graph, Node, Relationship, NodeMatcher
from py2neo.ogm import GraphObject
from neo4j import GraphDatabase

import queries
import mesh_info


HOST = 'bolt://localhost:7687'
AUTH = ('neo4j', 'password')

node_num = mesh_info.node_num
mesh = mesh_info.mesh_list
latitude = mesh_info.latitude_list
longitude = mesh_info.longitude_list
relation_dict = mesh_info.relation_dict_list


def create_mesh_graph():

    graphdb = Graph(HOST,auth=AUTH)
    for i in range(node_num):
        node = Node('Mesh')
        node['name'] = 'Mesh_' + str(mesh[i])
        node['meshcode'] = mesh[i]
        node['latitude'] = latitude[i]
        node['longitude'] = longitude[i]
        graphdb.merge(node, 'Mesh', 'name')

    driver = GraphDatabase.driver(HOST, auth=AUTH, encrypted=False)

    def node_association(tx, main_mesh, to_mesh, length):
        tx.run(queries.node_association,
               main_mesh=main_mesh, to_mesh=to_mesh, length=length)

    for i in range(node_num):
        main_mesh = mesh[i]
        north_mesh = relation_dict[i]['north']
        south_mesh = relation_dict[i]['south']
        north_south_length = 463
        west_mesh = relation_dict[i]['west']
        east_mesh = relation_dict[i]['east']
        west_east_length = 559

        if north_mesh != None:
            with driver.session() as session:
                session.write_transaction(node_association, main_mesh, north_mesh, north_south_length)

        if south_mesh != None:
            with driver.session() as session:
                session.write_transaction(node_association, main_mesh, south_mesh, north_south_length)

        if west_mesh != None:
            with driver.session() as session:
                session.write_transaction(node_association, main_mesh, west_mesh, west_east_length)

        if east_mesh != None:
            with driver.session() as session:
                session.write_transaction(node_association, main_mesh, east_mesh, west_east_length)


if __name__ == '__main__':
    create_mesh_graph()
