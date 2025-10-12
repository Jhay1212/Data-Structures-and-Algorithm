from random import randint
from typing import Any
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        
        def __str__(self):
            return str(self.val)
        
        def __repr__(self):
            return self.val

class CircularLinkedList:
    def __init__(self, val):
        new_node = Node(val)
        new_node.next = new_node
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
    def append(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
            
        self.length += 1
        
        
    def prepend(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        new_node.next = self.head
        self.head = new_node
        self.tail.next = new_node
        
        self.length += 1
        
        
    def insert(self, index: int, value: Any):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail.next = new_node
            new_node.next = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            new_node.next = temp.next
            temp = new_node
        self.length += 1
        
    def search(self, target):
        current = self.head 
        current_index = 0
        
        while current:
            if current.value == target:
                return current_index
            current = current.next
            current_index += 1
            if current == self.head:
                return -1
            
    def pop_first(self):
        popped_node = self.head
        if not self.length: return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    
    def pop(self):
        popped_node = self.tail
        if not self.length:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        
        else:
            temp = self.head 
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
            self.length -= 1
        
    def remove(self, index):
        if index > self.length or index < 0: raise IndexError("Index out of range error.")
        if index == 0:
            return self.pop_first()
        prev_node = self[index - 1]
        popped_node = self[index]
        prev_node.next = popped_node.next
        self.length -= 1
        return popped_node
    
    def destroy(self):
        self.head = None
        self.tail = None
        self.tail.next = None
        self.length = 0
        
    def __delete__(self):
        self.head = None
        self.tail = None
        self.tail.next = None
        self.length = 0
        # self.tail = self[self.length - 1]
        # self.tail.next = self.head
        # popped_node.next = None
        
        
    def __getitem__(self,  index: int):
        if index > self.length or index < 0: raise IndexError("Index out of range error.")
        current = self.head
        for i in range(index):
            current = current.next
            if current == self.head:
                break
        return current
    
    def __setitem__(self, index, value):
        if index > self.length or index < 0: raise IndexError("Index out of range error.")
        temp = self[index]
        if temp:
            temp.val = value
        
    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += str(temp.val)
            temp = temp.next 
            if temp == self.head:
                break
            if temp == self.tail:
                temp.next = self.head
            result += " => "
        return result
    
    
    

c = CircularLinkedList(1)
c.append(22)
for i in range(4):
    c.append(randint(i, 6))
    
c.prepend("jhay")
c.append("sorelia")
c.insert(3, "z22eef")
print(c.tail.next)
c[2] = "sunless"
print(c)