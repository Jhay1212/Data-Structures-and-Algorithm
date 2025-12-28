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


class MultiStock:
    def __init__(self, size):
        self.number_of_stacks = size
        self.c_list = [0] * (self.number_of_stacks * size)
        self.size = [0] * self.number_of_stacks
        self.stack_size = size
        
        
    def is_full(self, index):
        if self.size[index]  == self.stack_size:
            return True
        return False
        
        
    def is_empty(self, index):
        if not self.size[index]:
            return False
        return True
    
    def index_top(self, ind):
        offset = ind * self.stack_size
        return offset + self.size[ind] - 1
    
    def push(self, item, stack_index):
        if self.is_full(stack_index):
            return "Stacks are full"
        self.size[stack_index] += 1
        self.c_list[self.index_top(stack_index)] = item
        
        
    def pop(self, stack_index):
        if self.is_empty(stack_index):
            return "No stack empty"
        value = self.c_list[self.index_top(stack_index)]
        self.c_list[self.index_top(stack_index)] = 0
        self.size[stack_index] -= 1
        return value
    
    
multi_stock = MultiStock(3)
print(multi_stock)
print(multi_stock.is_full(0))
multi_stock.push("jhay", 0)
multi_stock.push("jhay", 0)
multi_stock.push("jhay", 0)
print(multi_stock.is_full(0))
        
    
    