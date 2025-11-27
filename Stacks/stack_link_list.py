class Node:
    def __init__(self, val):
        self.head = val
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.top = None
        self.size = 0         

    def push(self, val):
        new_node = Node(val)
        if self.size == 0:
            self.top = new_node
        new_node.next =self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty:
            return None
        popped_node = self.top
        self.top = self.top.next

        self.size -= 1
        return popped_node.head
    

    def peek(self):
        return self.top

    @property
    def is_empty(self):
        return self.length == 0
    
    
stack = StackLinkedList()
stack.push(1)
stack.push(12)
print(stack.pop())
