class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''
ancestors = []


def bst_traverse(curr_node, search_node):
    ancestors.append(curr_node)
    if (curr_node.info == search_node):
        return
    if (search_node > curr_node.info):
        bst_traverse(curr_node.right, search_node)
    elif (search_node < curr_node.info):
        bst_traverse(curr_node.left, search_node)


def lca(root, v1, v2):
    global ancestors
    bst_traverse(root, v1)
    v1_ancestors = ancestors.copy()

    ancestors = []
    bst_traverse(root, v2)
    v2_ancestors = ancestors.copy()

    return [i for i in v1_ancestors if i in v2_ancestors][-1]


tree = BinarySearchTree()
# t = int(input())

arr = list(map(int, '8 4 9 1 2 3 6 5'.split()))

for i in range(len(arr)):
    tree.create(arr[i])

v = [1, 2]

ans = lca(tree.root, v[0], v[1])
print(ans.info)
