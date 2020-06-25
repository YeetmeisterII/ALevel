from typing import Set


class Edge:
    edge_instances = []

    def __init__(self, node1: 'Node', node2: 'Node', distance: int):
        if (nodes := {node1, node2}) in map(lambda edge: edge.nodes(), self.edge_instances):
            raise Exception("Edge already exists.")
        self.edge_instances.append(self)
        self._nodes = nodes
        self._distance = distance

    def __repr__(self):
        nodes = list(self._nodes)
        return f"{nodes[0]} & {nodes[1]} of distance {self._distance}"

    def nodes(self) -> Set['Node']:
        return self._nodes.copy()

    def distance(self):
        return self._distance
