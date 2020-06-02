from neo4j import GraphDatabase, Transaction, Session

"""
[Node]
:Meshcode{mesh:-,  lat:-, lng:-}​​
:Pole​{mesh:-, lat:-, lng:-}​
:Charger​{mesh:-,  date:-, lat:-, lng:-, power:-, ...}​
:Point​{mesh:-, date:-, lat:-, lng:-, dense:-, ...}​
:EV​{mesh:-, date:-, lat:-, lng:-, helth:-,...}​

[Relationship]
:Length​{len:-}​
:Density​{date:-, dense:-, }​
"""

URL = 'bolt://localhost:7687'
AUTH = ('neo4j', 'passwd')



statemant = "CREATE (mc:Meshcode {mesh:, )"

driver = GraphDatabase.driver(URL, auth=AUTH, encrypted=False)

# CREATE Meshcode node
def create_mesh_node(tx, meshcode, lat, lng):
    tx.run("MERGE (:Meshcode {meshcode:"f'{meshcode}'
    ",location: point({latitude:"f'{lat}'",longitude:"f'{lng}'"})})",
    meshcode=meshcode, lat=lat, lng=lng)
    


with driver.session() as session:
    session.write_transaction(create_mesh_node, '53363085', 35.650361, 136.072261)

driver.close()

# CREATE Point node