from typing import List, Dict, Union

from PathFinding.edge import Edge
from PathFinding.node import Node


class Dijkstra:
    def __init__(self, starting_node: 'Node', ending_node: 'Node', nodes: List[Node], edges: List[Edge]):
        if not {starting_node, ending_node}.issubset(nodes):
            raise Exception('Start or ending node is not in the list of nodes')
        self._starting_node = starting_node
        self._ending_node = ending_node
        self._unvisited_nodes = nodes
        self._unchecked_edges = edges
        self._checked_edges = []

    def run(self) -> Dict[str, Union[int, list]]:
        self._ending_node.set_shortest_path_zero()
        next_node = None
        while next_node != self._starting_node:
            self._unvisited_nodes.sort(key=lambda node: node.shortest_path())
            next_node = self._unvisited_nodes.pop(0)
            self._visit_node(next_node)
        return self._get_result()

    def _visit_node(self, node: 'Node'):
        edges = self._find_edges(node)
        for edge in edges:
            pair_on_edge = list(edge.nodes())
            previous_node = pair_on_edge[0] if node == pair_on_edge[1] else pair_on_edge[1]
            distance = node.shortest_path() + edge.distance()
            previous_node.check_shortest_path(distance, node)

    def _get_result(self):
        distance = self._starting_node.shortest_path()
        final_path = self._get_path_to_end(self._starting_node)
        return {'distance': distance, 'path': final_path}

    def _get_path_to_end(self, node: 'Node'):
        path_string = node.name()
        while node != self._ending_node:
            node = node.next_node()
            path_string += f" => {node.name()}"
        return path_string

    def _find_edges(self, node) -> List['Edge']:
        node_edges = [edge for edge in self._unchecked_edges if node in edge.nodes()]
        for edge in node_edges:
            self._unchecked_edges.remove(edge)
            self._checked_edges.append(edge)
        return node_edges
