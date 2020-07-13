query = '''
CREATE (n1:CrossPoints) 
CREATE (n2:CrossPoints) 
CREATE (n1)-[l1:LENGTH]->(n2) 
CREATE (n1)<-[l2:LENGTH]-(n2) 
SET n1.mesh=$n1_mesh, n1.longitude=$n1_lng, n1.latitude=$n1_lat 
SET n2.mesh=$n2_mesh, n2.longitude=$n2_lng, n2.latitude=$n2_lat 
SET l1.len=$l1_len, l2.len=$l2_len 
'''

query1 = '''
MERGE (n1:CrossPoints {mesh:$n1_mesh, longitude:$n1_lng, latitude:$n1_lat}) 
MERGE (n2:CrossPoints {mesh:$n2_mesh, longitude:$n2_lng, latitude:$n2_lat}) 
CREATE (n1)-[l1:LENGTH {len:$l1_len}]->(n2) 
CREATE (n1)<-[l2:LENGTH {len:$l2_len}]-(n2) 
'''

node_association = '''
MATCH (main_node:Mesh {meshcode:$main_mesh}),
      (to_node:Mesh {meshcode:$to_mesh})
MERGE (main_node)-[:LENGTH {length:$length}]->(to_node)
MERGE (main_node)<-[:LENGTH {length:$length}]-(to_node)
'''