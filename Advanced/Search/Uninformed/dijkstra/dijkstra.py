from numpy import array, append, delete
from cost_node import cost_node as node
from pandas import DataFrame

class dijkstra:
    # Make dijkstra table
    class my_dijkstra_table:

        # Make dikstra table row class
        class my_dijkstra_table_row:
            def __init__(self, node, shortest_distance, prev_node):
                self.node= node
                self.shortest_distance = shortest_distance
                self.prev_node = prev_node
                self.is_visited= False

            def visited(self):
                self.is_visited= True

            def unvisiting(self):
                self.is_visited= False

        def __init__(self, node):
            self.__rows= {}
            self.__add_row(node, 0)

        # Make a function ro arrange a node, wether to add them to the table, update it, or ignore it
        def arrange_node(self, node, distance=None, prev_node=None, echo=False):
            if(not self.is_node_in_table(node)):
                self.__add_row(node, distance, prev_node, echo)
            elif(distance<self.__rows[node].shortest_distance):
                self.__update_row(node, distance, prev_node, echo)

        # Function to add row
        def __add_row(self, node, shortest_distance, prev_node=None, echo= False):
            if(echo):
                print(f'Adding {node.get_data()} with {shortest_distance} distance to dijkstra table..')
            self.__rows[node]= self.my_dijkstra_table_row(node, shortest_distance, prev_node)

        # Function to update row
        def __update_row(self, node, shortest_distance, prev_node, echo=False):
            if(echo):
                print(f'Updating {node.get_data()}, shortest distance from {self.__rows[node].shortest_distance} to {shortest_distance} on dijkstra table..')
            self.__rows[node].shortest_distance = shortest_distance
            self.__rows[node].prev_node = prev_node

        # Function to get the nearest row left
        def get_nearest_row(self):
            distance= None
            node= None

            for i in self.__rows.keys():
                if(not self.__rows[i].is_visited):
                    if(distance is None or self.__rows[i].shortest_distance<distance):
                        node= self.__rows[i].node
                        distance= self.__rows[i].shortest_distance

            return node, distance

        def visiting_node(self, node):
            self.__rows[node].visited()

        def clear_visiting_history(self):
            for i in self.__rows.keys():
                self.__rows[i].unvisiting()

        def is_node_in_table(self, node):
            if(node in self.__rows.keys()):
                return True
            else:
                return False

        def get_previous_row(self, node):
            if(self.is_node_in_table(node)):
                return self.__rows[node].prev_node
            else:
                return None

        def get_rows_cost(self, node):
            if(self.is_node_in_table(node)):
                return self.__rows[node].shortest_distance
            else:
                return None

        def get_table_row_list(self):
            raw_rows= []

            for key, item in self.__rows.items():
                data= item.node
                if(data is not None):
                    data= data.get_data()

                cost= item.shortest_distance

                prev= item.prev_node
                if(prev is not None):
                    prev= prev.get_data()

                raw_rows.append([data, cost, prev])

            return raw_rows


    def __init__(self, start_node=None, echo=False):
        self.__visited_node = array([])
        self.__dijkstra_table= self.my_dijkstra_table(start_node)

        if (start_node is not None):
            if (not isinstance(start_node, node)):
                print('Start node is not a node')
                return

        self.__start_node= start_node
        self.__echo = echo

    def set_start(self, start_node):
        if (not isinstance(start_node, node)):
            print('Start node is not a node')
            return

        self.__start_node= start_node

    def search_shortest_path(self, node):
        self.__visited_node= array([])
        self.__dijkstra_table.clear_visiting_history()

        self.traverse()
        traversed_node, total_cost= self.find_the_path(node)

        if traversed_node is not None and total_cost is not None:
            print(f'The shortest path: {self.backtrack(traversed_node)}')
            print(f'Total cost / distance: {total_cost}')
        else:
            print('Data is not found on the graph')


    def traverse(self):
        while(self.__dijkstra_table.get_nearest_row() is not None):
            curr_node, curr_distance= self.__dijkstra_table.get_nearest_row()

            if(curr_node is None):
                if(self.__echo):
                    print('<--- All nodes in graph has been traversed --->')
                return

            if(self.__echo):
                print(f'Visiting {curr_node.get_data()} :')

            self.__dijkstra_table.visiting_node(curr_node)
            self.__visited_node = append(self.__visited_node, curr_node)

            for adj_node in curr_node.adjacent_cost_list:
                if(adj_node[0] not in self.__visited_node):
                    curr_adj_node= adj_node[0]
                    curr_cost= adj_node[1] + curr_distance

                    if (self.__echo):
                        curr_adj_node_data = curr_adj_node
                        if curr_adj_node is not None:
                            curr_adj_node_data = curr_adj_node.get_data()

                        curr_node_data = curr_node
                        if curr_node is not None:
                            curr_node_data = curr_node.get_data()

                        print(f'Looking {curr_adj_node_data} from {curr_node_data}')

                    self.__dijkstra_table.arrange_node(curr_adj_node, curr_cost, curr_node, self.__echo)


    def find_the_path(self, node):
        if(self.__dijkstra_table.is_node_in_table(node)):
            traversed_node= [node]
            total_cost= self.__dijkstra_table.get_rows_cost(node)

            curr_node= node
            prev_node= self.__dijkstra_table.get_previous_row(curr_node)

            traversed_node.append(prev_node)

            while(True):
                curr_node= prev_node
                prev_node= self.__dijkstra_table.get_previous_row(curr_node)

                if(prev_node is None):
                    break

                traversed_node.append(prev_node)

            traversed_node.reverse()

            return traversed_node, total_cost

        else:
            return None, None

    def show_dijkstra_table(self):
        row_list= self.__dijkstra_table.get_table_row_list()

        table= DataFrame(data=row_list, columns=['Node', 'Shortest Distance from Start', 'Prev Node'])
        print(table)

    def backtrack(self, traversed_node):
        temp_string = ''

        for i in traversed_node:
            temp_string += i.get_data()

            if i != traversed_node[-1]:
                temp_string += ' -> '

        return temp_string