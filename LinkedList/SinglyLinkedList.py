class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
        
    def __eq__(self, value):
        return self.value == value
    
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
            
    def remove(self, index):
        if index > self.length or index < 0:
            raise IndexError()
        if index == 0:
            return self.pop_first()
        prev_node = self[index - 1]
        popped_node = self[index]
        prev_node.next = self[index].next
        popped_node.next = None
        self.length -= 1
        return popped_node
            
            
    def search(self, value):
        temp = self.head
        index = 0
        while temp:
            if temp.value == value:
                return index
            temp = temp.next
            index += 1
            
        else:
            return "Index does not exist"
        
        
    def pop(self):
        popped_node = self.tail
        if not self.length:
            return None 
    
        if self.length == 1:
            self.head = self.tail = None
            return popped_node
        temp = self.head
        while temp.next is not self.tail:
            temp = temp.next
        self.tail = None
        self.length -= 1
        return popped_node
    
    def pop_first(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return 
        popped_node = self.head
        self.head = self.head.next
        popped_node.next = None
        self.length -= 1
        return popped_node      
    
    def __del__(self):
        self.head = None 
        self.tail = None
        self.length = 0
        return  
    
     
    def __getitem__(self, index):
        temp = self.head
        current_index = 0
        while temp:
            if index == current_index:
                return temp.value
            temp = temp.next
            current_index += 1
        else:
            return -1
        
    def __setitem__(self, index, value):
        if index > self.length: raise IndexError("Index out of range")
        temp = self.head
        current_index = 0
        while temp:
            if index == current_index:
                temp.value = value
            temp = temp.next
            current_index += 1
        else:
            return -1

    def __eq__(self, other):
        if not(isinstance(other, LinkedList)): return False
        a, b = self.head, other.head
        while a and b:
            if a.value != b.value:
                return False
            a = a.next
            b = b.next
        return False
    
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

linked1[2] = 999
print(linked1[2])

# linked1.insert(Node(69), 3)
# linked1.traverse()
print(linked1.search(20))
print(linked1)

