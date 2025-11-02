class Node:
    def __init__(self, value):
        self.head = value
        self.next = None
        self.prev = None
        self.value = value
    def __str__(self):
        return str(self.value)

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, val):
        new_node = Node(value=val)
        if not self.length:
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
            
            
    def insert(self, index, value):
        if index < self.length or index > self.length: raise IndexError("Out of range")
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            self.append(value)
        new_node = Node(value)
        temp_node = self[index-1]
        new_node.next = temp_node.next
        new_node.prev = temp_node    
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
    def prepend(self, value):
        new_node = Node(value)
        if not self.length:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def find(self, index):
        if index > self.length or index < 0: raise IndexError("Out of range")
        current_node = self.head
        while current_node:
            if current_node.value == index:
                return current_node
            current_node = current_node.next
            if current_node == self.head: break
        return -1
    
    def pop(self):
        if self.length == 0:
            raise "List is empty"
        if self.length == 1:
            self.head = None
            self.tail = None
            return None
        popped_tail = self.tail
        self.tail = self.tail.prev
        popped_tail.next = None
        popped_tail.prev = None
        self.tail.next = self.head
        self.head.prev = self.tail
        self.length -= 1
        return popped_tail
    
    def remove(self, index):
        if index < 0 or index > self.length: raise IndexError("Out of range")
        if index == 0:
            return self.pop_head()
        if index == self.length - 1:
            return self.pop()
        temp_node = self[index - 1]
        popped_node = self[index]
        temp_node.next = popped_node.next
        popped_node.next.prev = temp_node
        self.length -= 1
        return popped_node
    
    def __del__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def __getitem__(self, index):
        """
        Returns the node at the given index.
        
        If the index is less than half of the list length so this array needs to be sorted 
        
        it will traverse the list from the head node.
        Otherwise, it will traverse the list from the tail node.
        """
        current_node = None
        if index < self.length  // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return current_node
    
    
    def pop_head(self):
        if self.length == 1:
            self.head = None
            self.tail = None
            return None
        
        popped_node = self.head
        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head
        
        self.length -= 1
        return popped_node
    def __setitem__(self, index, value):
        current_node = Node(value)
        if index > self.length or index < 0: raise IndexError("Out of range")
        if index < self.length  // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        current_node.head = value
    
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
            if current_node == self.head: break
            
    def __reverse__(self):
        current_node = self.tail
        while current_node:
            print(current_node.head)
            current_node = current_node.prev
            if current_node == self.tail: break
        
        
    def __str__(self):
        current_node = self.head
        result = ""
        while current_node:
            result += str(current_node.head)
            current_node = current_node.next
            if current_node == self.head: break
            result += "<->"
        return result
    
    def __eq__(self, other):
        if not(isinstance(other, DoubleLinkedList)): return False
        if self.length != other.length: return False
        a, b = self.head, other.head
        while a and b:
            print(a, b)
            if a.value != b.value:
                return False
            a = a.next
            b = b.next
            if a == self.head: break
        return True
        
    
            
cc = DoubleLinkedList()
cc2 = DoubleLinkedList()
cc.append(12)
cc.append(15)


cc2.append(12)
cc2.append(15)

print(cc == cc2)
print(cc, "\n", cc2)