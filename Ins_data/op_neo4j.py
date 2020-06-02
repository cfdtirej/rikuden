import csv
import datetime

from neo4j import GraphDatabase

HOST = 'bolt://localhost:7687'
AUTH = ('neo4j', 'passwd')

driver = GraphDatabase.driver(HOST, auth=AUTH , encrypted=False)

def create_person(driver, name):
    with driver.session() as session:
        return session.run(
            "CREATE (a:Person {name:$name})"
            "RETURN id(a)", name=name).single().value()
