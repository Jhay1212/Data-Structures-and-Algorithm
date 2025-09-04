from random import randint
class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

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
            result += "=>"
        return result
            
    
    def a(self, val):
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node = self.head
            self.tail = new_node
c = CircularLinkedList(1)
c.append(22)
for i in range(4):
    c.append(randint(i, 6))
print(c)