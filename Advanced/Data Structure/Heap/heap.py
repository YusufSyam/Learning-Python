# Min-heap implementation (tree way)

from heap_node import heap_node as node

import math

class heap:
    node_dict= {}

    def __init__(self, data= None):
        self.size= 1

        root_node= node(data)
        root_node.position= self.size
        self.node_dict[self.size]= root_node
        self.size+= 1
        # insert_node_position(self.root)

    # def insert_node_position(self, insert_node):
    #     if insert_node is None:
    #         return
    #
    #     insert_node.position= self.size
    #     self.size+= 1

    def insert(self, data= None):
        insert_node= node(data)
        insert_node.position= self.size

        if self.node_dict[1] is None:
            self.node_dict[1]= insert_node

            return

        parent= self.node_dict[self.get_top_node_position()]
        if self.size%2==0:
            parent.left= insert_node
        else:
            parent.right= insert_node

        insert_node.parent= parent
        self.node_dict[self.size]= insert_node
        self.size+= 1
        self.sorting_inserted_node(insert_node)

        print('\n-------------------')
        self.show_dict()


    def sorting_inserted_node(self, justify_node):
        curr_node= justify_node

        while True:
            if curr_node.position==1:
                # print(f'{curr_node.data} reached the top')
                break

            curr_parent= self.node_dict[self.get_top_node_position(curr_node.position)]

            # print('\n')
            # self.show_dict()
            # print('\n')

            if curr_node.data<curr_parent.data:
                # print(f'{curr_node.data} going up, passed {curr_parent.data}')

                curr_parent_parent= curr_parent.parent
                curr_parent_left= curr_parent.left
                curr_parent_right= curr_parent.right
                curr_parent_position= curr_parent.position

                curr_parent.position= curr_node.position
                curr_parent.right= curr_node.right
                curr_parent.left= curr_node.left
                curr_parent.parent= curr_node

                if curr_parent.right is not None:
                    curr_parent.right.parent= curr_parent

                if curr_parent.left is not None:
                    curr_parent.left.parent= curr_parent

                curr_node.parent= curr_parent_parent
                curr_node.position= curr_parent_position

                # print(curr_parent_right.data)
                # print(curr_node.data)

                if curr_parent_right==curr_node:
                    # print('DI kanan!')
                    curr_node.right= curr_parent
                    curr_node.left= curr_parent_left

                    try:
                        curr_node.left.parent= curr_node
                    except:
                        pass

                else:
                    # print('DI kiri!')
                    curr_node.left= curr_parent
                    curr_node.right= curr_parent_right

                    try:
                        curr_node.right.parent= curr_node
                    except:
                        pass

                if curr_parent_parent is not None:
                    if curr_parent_position%2==0:
                        # print('parent kiri!')
                        curr_parent_parent.left = curr_node
                    else:
                        # print('parent kanan!!')
                        curr_parent_parent.right = curr_node

                self.node_dict[curr_node.position]= curr_node
                self.node_dict[curr_parent.position] = curr_parent
            else:
                break

    def remove(self, data):
        existed_node_data= [i.data for i in self.node_dict.values()]

        if data not in existed_node_data:
            print('Data is not existed on the heap tree')
            return

        remove_node_position= existed_node_data.index(data) + 1

        latest_inserted_node= self.node_dict[self.size-1]
        latest_inserted_node.left= self.node_dict[remove_node_position].left
        latest_inserted_node.right= self.node_dict[remove_node_position].right
        latest_inserted_node.position= self.node_dict[remove_node_position].position
        latest_inserted_node.parent= self.node_dict[remove_node_position].parent

        self.node_dict[remove_node_position]= latest_inserted_node
        del self.node_dict[self.size-1]

        if self.node_dict[remove_node_position].right is not None:
            self.node_dict[remove_node_position].right.parent = self.node_dict[remove_node_position]

        if self.node_dict[remove_node_position].left is not None:
            self.node_dict[remove_node_position].left.parent = self.node_dict[remove_node_position]

        self.sorting_deleted_node(latest_inserted_node)
        self.size-= 1
        # print(f'Data existed: {self.node_dict[existed_node_data.index(data)+1].data}')

    def sorting_deleted_node(self, justify_node):
        # TODO
        pass

    def get_top_node_position(self, n= None):
        if n is None:
            n= self.size

        return n//2

    def show_dict(self):
        for i in self.node_dict:
            curr_node= self.node_dict[i]

            try:
                left_node= curr_node.left.data
            except:
                left_node= 'none'

            try:
                right_node= curr_node.right.data
            except:
                right_node= 'none'

            try:
                parent_node= curr_node.parent.data
            except:
                parent_node= 'none'

            print(f'index-{curr_node.position} = {curr_node.data}, left= {left_node}, right= {right_node}, parent= {parent_node}')