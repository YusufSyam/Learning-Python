from numpy import array, append, delete
from node import node

class breadth_first_search:
    class my_queue:
        def __init__(self):
            self.queue = array([])

        def enqueue(self, data):
            self.queue = append(self.queue, data)

        def dequeue(self):
            if (not self.is_empty()):
                self.queue = delete(self.queue, 0)
            else:
                print(self.__are_empty())

        def clear(self):
            self.queue= array([])

        def is_empty(self):
            return self.queue.size == 0

        def __are_empty(self):
            return 'There is no data left on the queue'

        @property
        def front(self):
            return self.queue[0] if (not self.is_empty()) else self.__are_empty()

        @property
        def rear(self):
            return self.queue[len(self.queue) - 1] if (not self.is_empty()) else self.__are_empty()

        @property
        def data(self):
            return self.queue

    def __init__(self, start_node=None, echo=False):
        self.__queue= self.my_queue()
        self.__visited_node= array([])
        self.__node_behind= {}

        if (start_node is not None):
            if(not isinstance(start_node, node)):
                print('Start node is not a node')
                return
            else:
                self.__queue.enqueue(start_node)

        self.__echo= echo

    def set_start(self, start_node):
        if (not isinstance(start_node, node)):
            print('Start node is not a node')
            return

        if (not self.__queue.is_empty()):
            self.__queue.clear()

        self.__queue.enqueue(start_node)

    def search(self, data):
        self.__visited_node= array([])
        self.__node_behind= {}

        traverse_result= self.traverse(data)

        if(traverse_result is None):
            print('There is no {data} on the graph')
        else:
            print(f'Data {data} has been found!\nBacktrack:')
            print(self.backtrack(traverse_result))

    def backtrack(self, node):
        if(self.__node_behind[node] in self.__node_behind.keys()):
            return f'{node.get_data()} <- {self.backtrack(self.__node_behind[node])}'
        else:
            return f'{node.get_data()} <- {self.__node_behind[node].get_data()}'

    def traverse(self, data):
        while(not self.__queue.is_empty()):
            curr_node= self.__queue.front
            self.__visited_node= append(self.__visited_node, curr_node)

            if(data==curr_node.get_data()):
                return curr_node

            adj_node_string= ''
            for adj_node in curr_node.adjacent_list:
                if(not adj_node in self.__visited_node):
                    self.__queue.enqueue(adj_node)
                    self.__visited_node= append(self.__visited_node, adj_node)
                    self.__node_behind[adj_node]= curr_node

                    adj_node_string+= f'{adj_node.get_data()}, '

            if (self.__echo):
                print(f'Visiting {curr_node.get_data()} ..', end='')

                if(adj_node_string is not ''):
                    print(f' adding {adj_node_string.strip(", ")} to the queue')
                else:
                    print()

            self.__queue.dequeue()

        return None






