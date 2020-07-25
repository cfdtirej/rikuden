from neo4j import GraphDatabase
from py2neo import Graph
from py2neo.matching import *

import query
import settings


def merge_tx(tx, north, south, west, east, name, meshcode, latitude, longitude, ns_length, we_length):
    tx.run(
        query.merge_charger,
        north=north,
        south=south,
        west=west,
        east=east,
        name=name,
        meshcode=meshcode,
        latitude=latitude,
        longitude=longitude,
        ns_length=ns_length,
        we_length=we_length
    )


def update_tx(tx, label, north, south, west, east,
              name, meshcode, latitude, longitude, time, used_latest, stored_latest,
              used_after_030, used_after_060, used_after_090,
              used_after_120, used_after_150, used_after_180,
              stored_after_030, stored_after_060, stored_after_090,
              stored_after_120, stored_after_150, stored_after_180,
              ns_length, we_length):
    run_query = query.update_charger.replace('$Label', label)
    tx.run(
        run_query,
        north=north, south=south, west=west, east=east,
        name=name, meshcode=meshcode, latitude=latitude, longitude=longitude,
        time=time, used_latest=used_latest, stored_latest=stored_latest,
        used_after_030=used_after_030, used_after_060=used_after_060, used_after_090=used_after_090,
        used_after_120=used_after_120, used_after_150=used_after_150, used_after_180=used_after_180,
        stored_after_030=stored_after_030, stored_after_060=stored_after_060, stored_after_090=stored_after_090,
        stored_after_120=stored_after_120, stored_after_150=stored_after_150, stored_after_180=stored_after_180,
        ns_length=ns_length, we_length=we_length
    )


class ChargerGraph:

    def __init__(self, host, auth, **kwargs):
        self.host = host
        self.auth = auth
        self.property = kwargs

    def is_charger_graph(self):
        graphdb = Graph(self.host, auth=self.auth)
        nodes = NodeMatcher(graphdb)
        charger = nodes.match(self.property['node_label'], name=self.property['name'], time=self.property['time']).first()
        return charger

    def merge_charger_graph(self):
        driver = GraphDatabase.driver(self.host, auth=self.auth, encrypted=False)
        with driver.session() as session:
            session.write_transaction(
                merge_tx,
                self.property['north'],
                self.property['south'],
                self.property['west'],
                self.property['east'],
                self.property['name'],
                self.property['meshcode'],
                self.property['latitude'],
                self.property['longitude'],
                self.property['ns_length'],
                self.property['we_length']
        )

    def update_charger_graph(self):
        driver = GraphDatabase.driver(self.host, auth=self.auth, encrypted=False)
        with driver.session() as session:
            session.write_transaction(
                update_tx,
                self.property['Label'],
                self.property['north'],
                self.property['south'],
                self.property['west'],
                self.property['east'],
                self.property['name'],
                self.property['meshcode'],
                self.property['latitude'],
                self.property['longitude'],
                self.property['time'],
                self.property['used_latest'],
                self.property['stored_latest'],
                self.property['used_after_030'],
                self.property['used_after_060'],
                self.property['used_after_090'],
                self.property['used_after_120'],
                self.property['used_after_150'],
                self.property['used_after_180'],
                self.property['stored_after_030'],
                self.property['stored_after_060'],
                self.property['stored_after_090'],
                self.property['stored_after_120'],
                self.property['stored_after_150'],
                self.property['stored_after_180'],
                self.property['ns_length'],
                self.property['we_length']
            )
