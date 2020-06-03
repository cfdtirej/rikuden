"""Data insert to neo4j"""

from neo4j import GraphDatabase

import queries


URL = 'bolt://localhost:7687'
AUTH = ('neo4j', 'password')
driver = GraphDatabase.driver(URL, auth=AUTH, encrypted=False)

# query = '''
# CREATE (n1:CrossPoints) 
# CREATE (n2:CrossPoints) 
# CREATE (n1)-[l1:LENGTH]->(n2) 
# CREATE (n1)<-[l2:LENGTH]-(n2) 
# SET n1.mesh=$n1_mesh, n1.longitude=$n1_lng, n1.latitude=$n1_lat 
# SET n2.mesh=$n2_mesh, n2.longitude=$n2_lng, n2.latitude=$n2_lat 
# SET l1.len=$l1_len, l2.len=$l2_len 
# '''

def create_graph(tx):
    tx.run(queries.query1,
           n1_mesh=11, n1_lng=1, n1_lat=1, 
           n2_mesh=22, n2_lng=2, n2_lat=2, 
           l1_len=11, l2_len=12)



with driver.session() as session:
    session.write_transaction(create_graph)





