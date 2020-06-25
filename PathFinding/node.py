class Node:
    __node_instances = {}
    _next_node = None
    _shortest_path = float('inf')

    def __init__(self, name):
        if name in map(lambda node: node.name(), self.__node_instances.values()):
            raise Exception("Node already exists.")
        self.__node_instances.update({name: self})
        self._name = name

    def __repr__(self) -> str:
        return f'Node {self._name}'

    def __del__(self):
        del self.__node_instances[self._name]

    @classmethod
    def node_instances(cls, key: str) -> 'Node':
        return cls.__node_instances[key]

    def name(self) -> str:
        return self._name

    def shortest_path(self) -> int:
        return self._shortest_path

    def next_node(self) -> 'Node':
        return self._next_node

    def set_shortest_path_zero(self):
        self._shortest_path = 0

    def check_shortest_path(self, distance: int, previous_node: 'Node'):
        if distance < self._shortest_path:
            self._shortest_path = distance
            self._next_node = previous_node
