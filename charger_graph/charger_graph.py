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


def update_tx(tx, meshcode, time, used_latest, stored_latest,
              used_after_30min, used_after_60min, used_after_90min,
              used_after_120min, used_after_150min, used_after_180min,
              stored_after_30min, stored_after_60min, stored_after_90min,
              stored_after_120min, stored_after_150min, stored_after_180min):
    tx.run(
        query.update_charger,
        meshcode=meshcode,
        time=time,
        used_latest=used_latest,
        stored_latest=stored_latest,
        used_after_30min=used_after_30min,
        used_after_60min=used_after_60min,
        used_after_90min=used_after_90min,
        used_after_120min=used_after_120min,
        used_after_150min=used_after_150min,
        used_after_180min=used_after_180min,
        stored_after_30min=stored_after_30min,
        stored_after_60min=stored_after_60min,
        stored_after_90min=stored_after_90min,
        stored_after_120min=stored_after_120min,
        stored_after_150min=stored_after_150min,
        stored_after_180min=stored_after_180min
    )


class ChargerGraph:

    def __init__(self, host, auth, **kwargs):
        self.host = host
        self.auth = auth
        self.property = kwargs

    def is_charger_graph(self):
        graphdb = Graph(self.host, auth=self.auth)
        nodes = NodeMatcher(graphdb)
        charger = nodes.match(self.property['node_label'], name=self.property['name']).first()
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
                self.property['meshcode'],
                self.property['time'],
                self.property['used_latest'],
                self.property['stored_latest'],
                self.property['used_after_30min'],
                self.property['used_after_60min'],
                self.property['used_after_90min'],
                self.property['used_after_120min'],
                self.property['used_after_150min'],
                self.property['used_after_180min'],
                self.property['stored_after_30min'],
                self.property['stored_after_60min'],
                self.property['stored_after_90min'],
                self.property['stored_after_120min'],
                self.property['stored_after_150min'],
                self.property['stored_after_180min'],
            )

