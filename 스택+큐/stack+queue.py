from collections import deque

# stack
## collections 라이브러리를 사용해서 구현
stack = deque()

stack.append(4)
stack.append(3)
stack.append(9)
print(stack) # deque([4, 3, 9])

stack.pop()
print(stack) # deque([4, 3])

## 라이브러리 없이 구현
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop()
        
    def print_stack(self):
        print(self.items)
            
s = Stack()

s.push(1)
s.push(4)
s.push(9)
s.print_stack() # [1, 4, 9]

s.pop()
s.print_stack() # [1, 4]

# queue
## collections 라이브러리를 사용해서 구현
queue = deque()

queue.append(3)
queue.append(2)
queue.append(8)
print(queue) # deque([3, 2, 8])

queue.popleft()
print(queue) # deque([2, 8])

## 라이브러리 없이 구현
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.items.pop(0)
    
    def print_queue(self):
        print(self.items)

q = Queue()

q.enqueue(5)
q.enqueue(8)
q.enqueue(4)
q.print_queue() # [5, 8, 4]

q.dequeue()
q.print_queue() # [8, 4]