class Stack(list):
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def peek(self):
        if not self.items:
            raise "Stack empty"
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
    def __del__(self):
        self.items = []

        

    def pop(self):
        if not self.is_empty:
            raise "Stack is empty"
        return self.items.pop()
    
    @property
    def is_empty(self):
        return self.items == 0
    
    def __str__(self):
        if self.is_empty:
            print(self.is_empty)
            raise "Stack is empty"
        i = [str(x) for x in reversed(self.items)]
        return "->".join(i)
    


mystack = Stack()
mystack.push(12)
mystack.push(123)
mystack.push(124)
print(mystack.peek())

