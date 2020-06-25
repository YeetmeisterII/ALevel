from PathFinding.edge import Edge
from PathFinding.node import Node


class Consumer:
    def __init__(self, graph: dict):
        self._graph = graph
        self._nodes = self._create_nodes()
        self._edges = self._create_edges()
        self._nodes = list(self._nodes.values())

    def _create_nodes(self):
        nodes = {}
        for key in self._graph.keys():
            nodes.update({key: Node(key)})
        return nodes

    def _create_edges(self):
        edge_data = []
        for node1, edge_info in zip(self._graph.keys(), self._graph.values()):
            for node2, distance in zip(edge_info.keys(), edge_info.values()):
                if (data := {node1, node2, distance}) not in edge_data:
                    edge_data.append(data)

        edges = []
        for data in edge_data:
            distance = [i for i in data if type(i) == int][0]
            node1, node2 = [i for i in data if type(i) == str]
            edges.append(Edge(self._nodes[node1], self._nodes[node2], distance))
        return edges

    def nodes(self):
        return self._nodes.copy()

    def edges(self):
        return self._edges.copy()
