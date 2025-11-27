from typing import List, Sequence, Str
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, val):
        self.append(val)

    def dequuee(self):
        if not self.length:
            raise "Queue is empty already"
        return self.items.pop(0)
    
    def peek(self):
        if not self.items:
            return "Queue is empty"
        return self.items[0]
    
    def destroy(self):
        self.items = []

        

    def __str__(self):
        return "\n".join(str(x) for x in self.items)
    

q = Queue()
q.enque(12)
q.enque(123)
print(q)
