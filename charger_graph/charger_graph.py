from neo4j import GraphDatabase
from py2neo import Graph
from py2neo.matching import *
# from py2neo.ogm import GraphObject

import query
import settings


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

    def update_tx(self, tx):
        tx.run(
            query.update_charger,
            label=self.property['node_label'],
            name=self.property['name'],
            time=self.property['time'],
            latest_used=self.property['latest_used'],
            latest_stored=self.property['latest_store'],
            after_30min=self.property['after_30min'],
            after_60min=self.property['after_60min'],
            after_90min=self.property['after_90min'],
            after_120min=self.property['after_120min'],
            after_150min=self.property['after_150min'],
            after_180min=self.property['after_180min'],
        )

    def merge_tx(self, tx):
        tx.run(
            query.merge_charger,
            label=self.property['node_label'],
            name=self.property['name'],
            latitude=self.property['latitude'],
            longitude=self.property['longitude'],
            north=self.property['north'],
            south=self.property['south'],
            west=self.property['west'],
            east=self.property['east'],
            ns_length=self.property['ns_length'],
            we_length=self.property['we_length']
        )


if __name__ == '__main__':
    d = settings.data_dict
    # d['node_label'] = 'Mesh'
    # d['name'] = 'Mesh_543771144'
    c = ChargerGraph(settings.HOST, settings.AUTH, **d)
    print(c.is_charger())
    c.merge()
