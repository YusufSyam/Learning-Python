from node import node
from numpy import array, append

class depth_first_search:

    __stack_list= []
    __visited_node= array([])

    def __init__(self, start_node=None, echo=False):
        if (start_node is not None):
            if(not isinstance(start_node, node)):
                print('Start node is not a node')
                return
            else:
                depth_first_search.__stack_list.append((start_node))

        self.__echo= echo

    def set_start(self, start_node):
        if (not isinstance(start_node, node)):
            print('Start node is not a node')
            return

        if (len(depth_first_search.__stack_list)>0):
            depth_first_search.__stack_list.pop()

        depth_first_search.__stack_list.append((start_node))

    def search(self, data):
        self.__visited_node = array([])

        if (depth_first_search.__stack_list):
            curr_node = depth_first_search.__stack_list[0]

            if (not curr_node in self.__visited_node):
                self.__visited_node= append(self.__visited_node, curr_node)

                if(self.__echo):
                    print(f'Visiting {curr_node.get_data()} ..')

            if (curr_node.get_data() == data):
                traverse_result= curr_node
            else:
                traverse_result= self.traverse_adjacent(curr_node, data)

            if(traverse_result is None):
                print('There is no data on the graph')
            else:
                print('Data has been found!\nBacktrack: ', end='')
                self.backtrack()

        else:
            print('There is no start / head node or the start node is not an instance of node class\n\tDefine start node by dfs_instance.set_start(node)')

    def backtrack(self):
        while(depth_first_search.__stack_list):
            if(len(depth_first_search.__stack_list)>1):
                print(f'{depth_first_search.__stack_list[0].get_data()} -> ', end='')
            else:
                print(depth_first_search.__stack_list[0].get_data())

            depth_first_search.__stack_list.pop(0)

    def traverse_adjacent(self, node, data):
        for adj_node in node.adjacent_list():

            if (not adj_node in self.__visited_node):
                depth_first_search.__stack_list.append(adj_node)

                self.__visited_node= append(self.__visited_node, adj_node)

                if (self.__echo):
                    print(f'Visiting {adj_node.get_data()} ..')

                if(adj_node.get_data()==data):
                    return adj_node

                looking_in_adjacent = self.traverse_adjacent(adj_node, data)
                if (looking_in_adjacent is not None):
                    return looking_in_adjacent

        depth_first_search.__stack_list.pop()
        return None






