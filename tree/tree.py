from typing import Any
from Queue.linked_queue import Queue 


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        
    def __str__(self):
        return f"""
                    {self.data}
        |-----------            ---------------|
        |                                    |
        {self.left_child}            {self.right_child}
    """
        
class LinkedBinaryTree:
    def __init__(self):
        pass
        



def pre_order_traversal(root_node: TreeNode):
    if not root_node:
        return
    
    print(root_node.data)
    pre_order_traversal(root_node.left_child)
    pre_order_traversal(root_node.right_child)
    

def in_order_traversal(root_node: TreeNode):
    if not root_node:
        return 
    
    in_order_traversal(root_node.left_child)
    print(root_node.data)
    in_order_traversal(root_node.right_child)
    

def post_order_travel(root_node: TreeNode):
    if not root_node:
        return
    
    post_order_travel(root_node=root_node.left_child)
    post_order_travel(root_node=root_node.right_child)
    print(root_node.data)


def level_order_traversal(root_node: TreeNode):
    if not root_node:
        return
    else: 
        c_queue = Queue()
        c_queue.enqueue(root_node)
        
        while not (c_queue.is_empty()):
            root = c_queue.dequeue()
            print(root.value.data)
            if root.value.left_child:
                c_queue.enqueue(root.value.left_child)
            if root.value.right_child:
                c_queue.enqueue(root.value.right_chid)
                
def search_binary_tree(tree_node: TreeNode, target: Any):
    if not tree_node:
        return "Tree doesn't exist"
    else:
        custom_queue = Queue()
        custom_queue.enqueue(tree_node)
        
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value.data == target:
                return True  
            
def insert_node(root_node: TreeNode, node: TreeNode):
    if not root_node:
        root_node = node
    else: 
        custom_queue = Queue()
        custom_queue.dequeue()
        while not custom_queue.is_empty():
            root = custom_queue.dequeue()
            if root.value.left_child:
                custom_queue.enqueue(root.value.left_child)
            else:
                root.value.left_child = node 
                return "Node added"
            
            if root.value.right_child:
                custom_queue.enqueue(root.value.left_child)
            else:
                root.value.right_child = node
                return "Node added"   
            
def get_deepest_node(root_node: TreeNode):
    if not root_node:
        return
    else:
        custom_q = Queue()
        custom_q.enqueue(root_node)
        
        while not (custom_q.is_empty()):
            new_root = custom_q.dequeue()
            
            if new_root.value.left_child is not None:
                custom_q.enqueue(new_root.value.left_child)
            if new_root.value.right_child is not None:
                custom_q.enqueue(new_root.value.right_child)
                
        deepest_node = new_root.value
        return deepest_node
    

def delete_tree(root_node: TreeNode):
    if not root_node:
        return
    root_node.data = None
    root_node.left_child = None
    root_node.right_child = None
        
def delete_deepet_node(root_node: TreeNode, node: TreeNode):
    if not root_node:
        return
    else:
        c_queue = Queue()
        c_queue.enqueue(root_node)
        
        while not (c_queue.is_empty()):
            root = c_queue.dequeue()
            
            if root.value is node:
                root.value = None 
                return
            
            if root.value.right_child:
                if root.value.right_child is node:
                    root.value.right_child = None
                    return 'asdad'
                else:
                    c_queue.enqueue(root.value.right_child)
                    
            if root.value.left_child: 
                if root.value.left_child is node:
                    s = root.value.left_child 
                    root.value.left_child = None
                    return s
                else:
                    c_queue.enqueue(root.value.left_child)
                    
                    
def delete_node(root_node: TreeNode, target_node: TreeNode):
    if not root_node:
        return
    c_queue = Queue()
    c_queue.enqueue(root_node)
    while not c_queue.is_empty():
        root = c_queue.dequeue()
        if root.value.data == target_node:
            deep_node = get_deepest_node(root_node)
            root.value.data = deep_node.data