from mazeDetector import MazeDetector
import matplotlib.pyplot as plt
import networkx as nx


maze_detector = MazeDetector()
maze = maze_detector.get_graph('./mazes/not_even_a_maze.png')

maze_graph = nx.Graph()

for node in maze:
    maze_graph.add_node(node.get_id())
    print(node.get_adjacents())
    for neighbor in node.get_adjacents():
        maze_graph.add_edge(node.get_id(), neighbor.get_id())

nx.draw(maze_graph, with_labels=True)
plt.draw()
plt.show()