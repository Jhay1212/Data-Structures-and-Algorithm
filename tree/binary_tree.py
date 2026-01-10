class BinaryTree:
    """
    Binary tree when implemented in list
    """
    
    
    def __init__(self, size):
        self.list = size * [None]
        self.last_index = 0
        self.max_size = size
        
    def insert(self, node):
        if self.last_index + 1 == self.max_size:
            print('full')
            return "full"
        self.list[self.last_index+1] = node
        self.last_index += 1

    def pre_order_traversal(self, index):
        if index > self.last_index:
            return
        print(self.list[index])
        self.pre_order_traversal(index*2)
        self.pre_order_traversal(index*2 + 1)
        
    def in_order_traversal(self, index):
        if index > self.last_index:
            return
        
        self.in_order_traversal(index*2)
        print(self.list[index])
        self.in_order_traversal(index * 2 + 1)
        
      
    def post_order_traversal(self, index=1):
        if index > self.last_index:
            return 
        
        self.in_order_traversal(index * 2)
        self.in_order_traversal(index * 2 + 1)
        print(self.list[index])
    
    def level_order_traversal(self, index=1):
        for i in range(index, self.last_index):
            print(self.list[i])
        return
    
    def delete(self, value):
        if self.last_index == 0:
            return None
        
        for i in range(1, self.last_index + 1):
            if self.list[i] == value:
                self.list[i] = self.list[self.last_index]
                self.list[self.last_index] = None
                self.last_index -= 1
                print('item deleted')
                
binary_tree = BinaryTree(10)
binary_tree.insert("1")
binary_tree.insert(121212)
binary_tree.insert("123")
binary_tree.insert("askjdaksddf,ksfdk34346565")
binary_tree.insert("askjdaksd069 69 69 69 69 9")

# 
# binary_tree.pre_order_traversal(1)
# binary_tree.in_order_traversal(1)
# binary_tree.post_order_traversal()
binary_tree.delete("1")
binary_tree.level_order_traversal()