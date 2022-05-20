class heap_node:
    def __init__(self, data, left= None, right= None):
        self.data= data
        self.parent= None
        self.position= None
        self.left= left
        self.right= right