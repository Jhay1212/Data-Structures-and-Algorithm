class Node:
    def __init__(self, value):
        self.head = value
        self.next = None
        self.prev = None
        
    def __str__(self):
        return f"{self.prev} -> {self.head} -> {self.next}"

class DoubleLinkedList:
    def __init__(self, val):
        self.head = Node(val)
        self.tail = None
        self.length = 1
        
    def append(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = self.tail
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1