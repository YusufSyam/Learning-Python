# Importing our diy node-with-distance-for-each-adjacent class
from cost_node import cost_node as node

# For organizing visited node
from numpy import array, append

# For displaying the dijkstra table
from pandas import DataFrame

class dijkstra:

    # Make dijkstra table class, where we store and process information
    class my_dijkstra_table:

        # Make dikstra table row class, that has node, shortest distance from start node,
        # Previous node (node that gives the shortest distance), and a boolean is visited or not
        class my_dijkstra_table_row:
            def __init__(self, node, shortest_distance, prev_node):
                self.node= node
                self.shortest_distance = shortest_distance
                self.prev_node = prev_node
                self.is_visited= False

            # Function to change the is_visited state
            def visited(self):
                self.is_visited= True

            def unvisiting(self):
                self.is_visited= False

        # Constructor of dijkstra table, we can define the start node here
        def __init__(self, start_node=None):
            # Initializing dictionary where we put our dijkstra table row classes
            # The nodes will be the key even though we still store the node on the value which is the dijkstra table row class
            self.__rows= {}

            # Check if the start_node provided on the parameter is not none
            if start_node is not None:
                # Check wether the start node is a node, if so then we add that node as a dijkstra table row with 0 distance
                if not isinstance(start_node, node):
                    print('Start node is not a node')
                    return
                else:
                    self.__add_row(node, 0)


        # Make a function to arrange a node, wether to add them to the table, update it, or ignore it
        def arrange_node(self, node, distance=None, prev_node=None, echo=False):
            # If node is not in the row yet, then add it
            if(not self.is_node_in_table(node)):
                self.__add_row(node, distance, prev_node, echo)

            # If node is already in the row, and the distance parameter is smaller than its current distance,
            # Then update the distance as well as the previous node
            elif(distance<self.__rows[node].shortest_distance):
                self.__update_row(node, distance, prev_node, echo)

        # Function to add row
        def __add_row(self, node, shortest_distance, prev_node=None, echo= False):
            # Echo is parameter to decide wether to print the current state/process or not
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
            # First we define the distance and node, with value None, on most theory, we set the distance with a very big number or infinity
            # But for simplicity we can just fill it with None and then threat None value the same as we threat infinity number on the theory
            distance= None

            # node here will be filled and referred to the node with the smallest distance
            node= None

            # Looping for getting the shortest distance among unvisited node
            for i in self.__rows.keys():
                if(not self.__rows[i].is_visited):
                    if(distance is None or self.__rows[i].shortest_distance<distance):
                        node= self.__rows[i].node
                        distance= self.__rows[i].shortest_distance

            # Return the node and it's distance, there is possibility that node and distance is None
            # In which case there is no more unvisited node on the dijkstra table
            return node, distance

        # Function to set visiting node of a row is true
        def visiting_node(self, node):
            self.__rows[node].visited()

        # Function to unvisit all the rows on the table
        def clear_visiting_history(self):
            for i in self.__rows.keys():
                self.__rows[i].unvisiting()

        # Function to check if there is a row contain certain node on the table
        def is_node_in_table(self, node):
            if(node in self.__rows.keys()):
                return True
            else:
                return False

        # Function to get the previous row from a row contain the given node
        def get_previous_row(self, node):
            if(self.is_node_in_table(node)):
                return self.__rows[node].prev_node
            else:
                return None

        # Function to get row's cost / shortest distance
        def get_rows_cost(self, node):
            if(self.is_node_in_table(node)):
                return self.__rows[node].shortest_distance
            else:
                return None

        # Function to get table as 2d array
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


    # Constructor of dijkstra, if start node is provided and is a node, then add it as a start node
    def __init__(self, start_node=None, echo=False):
        # Make an empty array where we will put the visited node later
        self.__visited_node = array([])

        # Check if start node is provided on the parameter and if the start node is an instance of node
        if (start_node is not None):
            if (not isinstance(start_node, node)):
                print('Start node is not a node')
                return

        # Make an instance of dijkstra table
        self.__dijkstra_table= self.my_dijkstra_table(start_node)

        self.__start_node= start_node
        self.__echo = echo

    # def set_start(self, start_node):
    #     if (not isinstance(start_node, node)):
    #         print('Start node is not a node')
    #         return
    #
    #     self.__start_node= start_node

    # Function to search the shortest path from start to goal by going through all connected nodes around
    def search_shortest_path(self, goal):
        # Empty the visited node array so this function can be used repeatedly
        self.__visited_node= array([])
        self.__dijkstra_table.clear_visiting_history()

        # First we traverse through all nodes on the graph and
        # Calculate the shortest distance between start node and all nodes
        self.traverse()

        # Now on the dijkstra table all row except start node has the prev node,
        # Based on that we backtracking from the goal to start node by the following function
        traversed_node, total_cost= self.find_the_path(goal)

        # If node searched is on the graph, then print the shortest path as well as the total cost / distance
        if traversed_node is not None and total_cost is not None:
            print(f'The shortest path: {self.backtrack(traversed_node)}')
            print(f'Total cost / distance: {total_cost}')
        else:
            print('Data is not found on the graph')

    # Function for traversing all nodes on the graph
    def traverse(self):
        # Will keep looping until there is no more nearest node or unvisited node
        while(self.__dijkstra_table.get_nearest_row() is not None):
            # First we get current nearest node (row on the dijkstra table) and it's distance
            curr_node, curr_distance= self.__dijkstra_table.get_nearest_row()
            
            # If curr node is None, return from the function (?)
            if(curr_node is None):
                if(self.__echo):
                    print('<--- All nodes in graph has been traversed --->')
                return
            
            if(self.__echo):
                print(f'Visiting {curr_node.get_data()} :')
            
            # Mark current row (curr_node) as visited row on the dijsktra table
            self.__dijkstra_table.visiting_node(curr_node)
            
            # Mark current row (curr_node) as visited row on the visited_node array
            self.__visited_node = append(self.__visited_node, curr_node)
            
            # Why do we have 2 different visited node array? because \\ ... \\
            
            # Looping through all adjacent node from the current node
            for adj_node in curr_node.adjacent_cost_list:
                
                # Since curr_node.adjacent_cost_list returns array contains a node and it cost,
                # We put adj_node first element (which is the node) into condition
                # If the current adjacent node is not visited yet
                if(adj_node[0] not in self.__visited_node):
                    
                    # Now we define current adjacent node and it's cost
                    curr_adj_node= adj_node[0]
                    curr_cost= adj_node[1] + curr_distance
                    
                    # Condition to print the current process
                    if (self.__echo):
                        curr_adj_node_data = curr_adj_node
                        if curr_adj_node is not None:
                            curr_adj_node_data = curr_adj_node.get_data()

                        curr_node_data = curr_node
                        if curr_node is not None:
                            curr_node_data = curr_node.get_data()

                        print(f'Looking {curr_adj_node_data} from {curr_node_data}')
                       
                    # And then we sent them to dijkstra table to find the right action for this node
                    self.__dijkstra_table.arrange_node(curr_adj_node, curr_cost, curr_node, self.__echo)

    
    # Function to get the shortest path from start to end
    def find_the_path(self, node):
        # This function will return the goal node and its total cost from start node
        # First we make a condition, if the goal/searched node is on the graph, then do the statement below,
        # If else, then return None and None
        if(self.__dijkstra_table.is_node_in_table(node)):
            
            # First we make an array to put all the traversed node, the first elemen is the node from parameter which is the goal node
            traversed_node= [node]

            # Then we get the total cost from start to goal
            total_cost= self.__dijkstra_table.get_rows_cost(node)

            # Set the node as current node
            curr_node= node
            
            # Set the previous node
            prev_node= self.__dijkstra_table.get_previous_row(curr_node)

            # Append the previous node to the traversed_node array
            traversed_node.append(prev_node)
            
            # Looping until there is no previous node anymore
            while(True):
                
                # Set current node with prev_node
                curr_node= prev_node
                
                # Set prev_node with current_node's previous node
                prev_node= self.__dijkstra_table.get_previous_row(curr_node)
                
                # If prev_node is none, then break the loop
                if(prev_node is None):
                    break

                # Add the prev_node to the traversed_node array
                traversed_node.append(prev_node)
            
            # Reverse the array
            traversed_node.reverse()
            
            # Return both traversed node and it's cost
            return traversed_node, total_cost

        else:
            # Return both none
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
