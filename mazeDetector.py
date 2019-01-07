from node import Node
import cv2


class MazeDetector:

    def __init__(self):
         self.nodes = []
         self.maze_bounds = {'height': None,
                             'width' : None}
    
    def get_graph(self, image):
        binary_maze = self.get_binary_maze(image)
        self.maze_bounds['height'] = len(binary_maze)
        self.maze_bounds['width']  = len(binary_maze[0])
        available_positions = self.get_available_positions(binary_maze)
        graph = self.convert_to_nodes(available_positions)
        for node in graph:
            for other_node in graph:
                if node.get_position_sum() == other_node.get_position_sum() + 1 or node.get_position_sum() == other_node.get_position_sum() - 1:
                   node.add_adjacent_node(other_node)
        # print(binary_maze)
        return graph


    def get_binary_maze(self, image):
        gray_image  = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        binary_maze = cv2.threshold(gray_image, 127, 1, cv2.THRESH_BINARY)[1]
        return binary_maze
    
    def get_available_positions(self, binary_maze):
        # Find faster way using NIx
        available_positions = []
        for row_index, row in enumerate(binary_maze):
            for column_index, positon in enumerate(row):
                if row[column_index] == 1:
                    available_positions.append((row_index, column_index))
        return available_positions

    def convert_to_nodes(self, available_positions):
        nodes = []
        for index, position in enumerate(available_positions):
            node = Node([], position, "-", index)
            nodes.append(node)
        return nodes
    
    def get_id(self):
        return self.node_id