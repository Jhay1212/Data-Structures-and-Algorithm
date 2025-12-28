class Node:
    def __init__(self, val):
        self.head = val
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.head)
    
    def __repr__(self):
        return str(self.head)
    

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node

        self.tail.next = node
        self.tail = self.tail.next
        self.length += 1

    
    def prepend(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
        node.next = self.head
        self.head = node
        self.tail.next = node
        self.length += 1
        

    def __iter__(self):
        current_node = self.head
        while current_node.next:
            yield current_node
            current_node = current_node.next


    def __str__(self):
        current_node = self.head
        val = ""
        while current_node:
            val += str(current_node) + " -> "
            if current_node.next:
                current_node = current_node.next
        return val
    def __len__(self):
        return self.length

li = DoublyLinkedList()
li.append(1)
li.prepend(2)

print(li)