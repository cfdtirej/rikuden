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


def update_tx(tx, meshcode, time, latest_used, latest_stored,
              after_30min, after_60min, after_90min, after_120min, after_150min, after_180min):
    tx.run(
        query.update_charger,
        meshcode=meshcode,
        time=time,
        latest_used=latest_used,
        latest_stored=latest_stored,
        after_30min=after_30min,
        after_60min=after_60min,
        after_90min=after_90min,
        after_120min=after_120min,
        after_150min=after_150min,
        after_180min=after_180min
    )


class ChargerGraph:

    def __init__(self, host, auth, **kwargs):
        self.host = host
        self.auth = auth
        self.property = kwargs

    def is_charger(self):
        graphdb = Graph(self.host, auth=self.auth)
        nodes = NodeMatcher(graphdb)
        charger = nodes.match(self.property['node_label'], name=self.property['name']).first()
        return charger

    def update_charger_graph(self):
        driver = GraphDatabase.driver(self.host, auth=self.auth, encrypted=False)
        with driver.session() as session:
            session.write_transaction(
                update_tx,
                self.property['meshcode'],
                self.property['time'],
                self.property['latest_used'],
                self.property['latest_stored'],
                self.property['after_30min'],
                self.property['after_60min'],
                self.property['after_90min'],
                self.property['after_120min'],
                self.property['after_150min'],
                self.property['after_180min'],
            )

    def merge_cherger_graph(self):
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