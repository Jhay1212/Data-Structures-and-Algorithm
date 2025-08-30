class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    
    def __str__(self):
        return str(self.value)
    
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
        
    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1 
        
    def prepend(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def __str__(self):
        temp = self.head
        res = ""
        while temp is not None:
            res += str(temp.value)
            if temp.next is not None:
                res += " => "
            temp = temp.next
        print(res)
        return res
        
            
            
linked1 = LinkedList()
linked1.append(Node(20))
linked1.append(Node(22))

print(linked1)

