class PlateStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        
    def push(self, item):
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.appen(item)
            
    def pop(self):
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if not self.stacks:
            return None
        return self.stacks[-1].pop()
    
    def pop_at(self, index):
        if len(self.stacks):
            return self.stacks[index].pop()
        else:
            return None
        
        
        
class Stack:
    def __init__(self):
        self.list = []
        
    def __len__(self):
        return len(self.list)
    
    def push(self, item):
        self.list.append(item)
        return self.list
    
    def pop(self):
        if not self.list:
            raise "Empty stack"
        return self.list.pop()
    
    
class QueueViaStackL:
    def __init__(self):
        self.in_stack = Stack()
        self.out_stack = Stack()
        
    def enqueue(self, item): 
        self.in_stack.push(item)
        
    def dequeue(self):
        """
        Pop every item in the in stack and push it into out stack
        then store the pop item to th eresult
        """
        while len(self.in_stack):
            
            self.out_stack.push(self.in_stack.pop())
            
        result = self.out_stack.pop()
        while len(self.out_stack):
            self.in_stack.push(self.out_stack.pop())
        return result
    
    
class Cat:
    pass

class Dog:
    pass
    
class AnimalShelterQ:
    def __init__(self):
        self.cats = []
        self.dog  = []
        
    def enqueue(self, animal):
        if type(animal) == Cat:
            self.cats.append(animal)
        elif type(animal) == Dog:
            self.dog.append(animal)
            
    def dequeue_cat(self):
        if self.cats:
            cat = self.cats.pop(0)
            return cat
        return 'No cat on queue'
    
    def dequeue_dog(self):
        if self.dog:
            return self.dog.pop(0)
        
    def dequeue(self):
        if self.cats:
            return self.cat.pop(0)
        else:
            return self.dog.pop(0)