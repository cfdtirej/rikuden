import os
import pandas as pd
from py2neo import Graph, Node, Relationship
from geopy.distance import geodesic


URL = 'bolt://localhost:7687'
AUTH = ('neo4j', 'password')
pwd = os.getcwd()
df = pd.read_excel(pwd + '/16toyama500m.xlsx')
df_length = len(df)
l = [i for i in range(df_length)]
df_column = df.columns

mesh_array = list(df[df_column][df_column[0]][l])
lat_array = list(df[df_column][df_column[1]][l])
lng_array = list(df[df_column][df_column[2]][l])
location = (lat_array[1], lng_array[1])

distance = []
for i in range(1, df_length):
    location_next = (lat_array[i], lng_array[i])
    location_dist_m = geodesic(location, location_next).meters
    distance.append(location_dist_m)
    location = location_next

def create_node():
    graphdb = Graph(URL, auth=AUTH)

    before_node = Node('x_node')
    before_node['name'] = 'x_node' + str(1)
    before_node['mesh'] = mesh_array[1]
    before_node['latitude'] = float(mesh_array[1])
    before_node['longitude'] = float(mesh_array[1])
    
    graphdb.create(before_node)

    for i in range(2, df_length):
        mesh = mesh_array[i]
        lat = lat_array[i]
        lng = lng_array[i]

        node = Node('x_node')
        node['name'] = 'x_node' + str(i)
        node['mesh'] = mesh
        node['latitude'] = lat
        node['longitude'] = lng
        
        rel1 = Relationship(before_node, "LENGTH", node, length=distance[i-1])
        rel2 = Relationship(node, "LENGTH", before_node, length=distance[i-1])
        graphdb.create(rel1)
        graphdb.create(rel2)

        before_node = node
        
create_node()

