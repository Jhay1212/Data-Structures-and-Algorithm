from typing import Sequence
class Node:
    def __init__(self, val):
        self.val = val
        self.next 
    
    def __str__(self):
        return str(self.val)
        
        
class LinkedList(Sequence):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __iter__(self):
        curr_node = self.head
        
        while curr_node:
            yield curr_node
            curr_node.next
            
            
class Queue:
    def __init__(self):
        self.queue = LinkedList()
        
    def enqueue(self, value):
        new_node = Node(value)
        if not self.queue.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.queue.tail = new_node
            
    def is_empty(self):
        return self.queue.head is None
    
    def dequeue(self):
        if self.is_empty():
            return "No item in the queue"
        temp_node = self.queue.head 
        if self.queue.head  == self.queue.tail:
            self.head = None
            self.tail = None        
        else:
            self.queue.head = self.queue.head.next
            
    def peek(self):
        if self.is_empty():
            return "No item"
        return self.queue.head
    
    def destroy(self):
        if self.is_empty():
            return "No item"
        self.queue.head = None
        self.queue.tail = None