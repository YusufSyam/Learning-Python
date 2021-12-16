class cost_node:

    def __init__(self, data=None):
        self.__data= data
        self.__adjacent= []
        self.__adjacent_cost= {}

    def set_data(self, data):
        self.__data= data

    def get_data(self):
        return self.__data

    def add_adjacent(self, node, cost, first_addition=True):
        if(cost<0):
            print('Cost can not be negative, setting cost to 0...')
            cost= 0

        self.__adjacent.append(node)
        self.__adjacent_cost[node]= cost

        if(first_addition):
            node.add_adjacent(self, cost, first_addition= False)

    @property
    def adjacent_cost_list(self):
        return [(i, self.__adjacent_cost[i]) for i in self.__adjacent]

    @property
    def info(self):
        return f'Data: {self.__data}\nAdjacent List data: {[i.get_data() for i in self.__adjacent]}'