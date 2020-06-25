from PathFinding.algorithms import Dijkstra
from PathFinding.node import Node
from PathFinding.graph_consumer import Consumer

graph = {"A": {"B": 75, "C": 10},
         "B": {"A": 75, "F": 60, "D": 5},
         "C": {"A": 10, "F": 30, "E": 55},
         "D": {"B": 5, "I": 10, "F": 55, "G": 45},
         "E": {"C": 55, "J": 70},
         "F": {"B": 60, "D": 55, "G": 10, "C": 30},
         "G": {"D": 45, "F": 10, "H": 40},
         "H": {"G": 40, "J": 15},
         "I": {"D": 10, "J": 65},
         "J": {"I": 65, "H": 15, "E": 70}}

consumer = Consumer(graph)
nodes = consumer.nodes()
edges = consumer.edges()
algorithm = Dijkstra(starting_node=Node.node_instances('A'), ending_node=Node.node_instances('J'), nodes=nodes,
                     edges=edges)
print(algorithm.run())
