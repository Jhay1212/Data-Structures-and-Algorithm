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
        
    def insert(self, val, index):
        new_node = Node(val)
        if index > self.length or index < 0: raise IndexError("Index out of range error") # index out of range base casae

        
        if index == 0 and self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            # print((self.length + index), self.length, index)
            # if index < 0 and abs(self.length + index) < self.length:
            #     index =abs(self.length - index)
            #     print(index)
            temp_node = self.head
            for i in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1 
        
    def traverse(self):
        temp = self.head
        while temp:
            print(temp)
            temp = temp.next
            
            
    def search(self, value):
        temp = self.head
        while temp:
            if temp.value == value:
                return True
            temp = temp.next
        return "Value does not exist"
    
    
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
linked1.append(Node(21))
linked1.append(Node(23))

linked1.insert(Node(69), 3)
linked1.traverse()
print(linked1.search(21))
print(linked1)

