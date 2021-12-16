# Same class node as dfs
class node:

    def __init__(self, data=None):
        self.__data= data
        self.__adjacent= []
        self.traversed_before= None

    def set_data(self, data):
        self.__data= data

    def get_data(self):
        return self.__data
    
    def add_adjacent(self, node, first_addition=True):
        self.__adjacent.append(node)

        if(first_addition):
            node.add_adjacent(self, first_addition= False)

    def through_node(self, node):
        node.add_traversed_before(self)

    def add_traversed_before(self, node):
        self.traversed_before= node

    @property
    def adjacent_list(self):
        return self.__adjacent

    @property
    def info(self):
        return f'Data: {self.__data}\nAdjacent List data: {[i.get_data() for i in self.__adjacent]}'
