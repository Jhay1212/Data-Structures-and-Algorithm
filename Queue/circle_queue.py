

from typing import Any, Sequence


class CircledQueue:
    def __init__(self, max_size):
        self.items = max_size * [0]
        self.max_size = max_size
        self.start = -1
        self.top = -1

    def is_full(self):
        if self.top + 1 == self.start:
            return True
        return False
    
    def is_empty(self):
        return bool(self.items)

    def enqueue(self, val: Any):
        if self.is_full():
            return "Queue is full can not anymore object."
        self.top += 1
        if self.start == - 1:
            self.start = 0
        self.items[self.top] = val
        return 
    
    def dequeue(self, val: Any):
        if self.is_empty():
            raise "Queue is empty."
        first_element = self.items[self.start]
        start = self.start
        if self.start == self.stop:
            self.start -= 1
            self.top -= 1
        elif self.start + 1 == self.max_size:
            self.start = 0
        else:
            self.start += 1
        self.items[start] = None
        return first_element
    
    def peek(self):
        if self.is_empty():
            raise "Queue is empty."
        return self.items[self.start]
    
    def __destroy__(self):
        self.items = self.max_size * [0]
        self.start = - 1
        self.top = - 1

    def __str__(self):
        return " ".join(str(x) for x in self.items)
    

cq = CircledQueue(5)
cq.enqueue(12)
cq.enqueue(312)

print(cq)