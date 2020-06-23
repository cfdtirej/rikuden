from py2neo import Graph, Node, Relationship
from py2neo.ogm import GraphObject


def create_nodes():
    graph = Graph(
        'bolt://localhost:7687',
        auth=('neo4j', 'password')
    )

    Point1 = Node('Crossroad')
    Point1['meshcode'] = 100
    Point1['datetime'] = '2020-05-01'

    Point2 = Node('Crossroad')
    Point2['meshcode'] = 101
    Point2['datetime'] = '2020-05-02'

    Rel1 = Relationship(Point1, 'LENGTH', Point2)
    Rel1['length'] = 100

    Rel2 = Relationship(Point2, 'LENGTH', Point1)
    Rel1['length'] = 100

    # graph.create(Point1)
    # graph.create(Point2)
    graph.create(Rel1)
    graph.create(Rel2)

create_nodes()



