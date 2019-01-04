class Node:

    def __init__(self):
        self.adjacents = []
        self.position  = None
        self.visited   = False

    def __init__(self, adjacents, position):
        self.adjacents = adjacents
        self.position  = position
        self.visited   = False

    def set_position(position):
        self.position = position

    def add_adjacent_node(self, node):
        self.adjacents.append(node)

    def visit(self):
        self.visited = True
    
    def get_position_sum(self):
        return self.position[0] + self.position[1]

    def get_adjacents(self):
        return self.adjacents

    def get_position(self):
        return self.position

    def is_visited(self):
        return self.visited