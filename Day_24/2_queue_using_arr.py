# Implement Queue Using Array
# Problem Statement: Implement a First-In-First-Out (FIFO) queue using an array. The implemented queue should support the following operations: push, dequeue, pop, and isEmpty.

# Implement the ArrayQueue class:
# void push(int x): Adds element x to the end of the queue.
# int pop(): Removes and returns the front element of the queue.
# int peek(): Returns the front element of the queue without removing it.
# boolean isEmpty(): Returns true if the queue is empty, false otherwise.

from collections import deque
class myQueue:
    def __init__(self, n):
        self.queue= deque()
        self.capacity = n

    # Check if queue is empty
    def isEmpty(self):
        return len(self.queue)==0
        
    # Check if queue is full
    def isFull(self):
        return len(self.queue)==self.capacity
    
    # Enqueue
    def enqueue(self, x):
        if self.isFull():
            return -1
        self.queue.append(x)
    
    # Dequeue  
    def dequeue(self):
        if self.isEmpty():
            return -1
        return self.queue.popleft()
     
    # Get front element
    def getFront(self):
        if self.isEmpty():
            return -1 
        return self.queue[0]
        
    # Get rear element
    def getRear(self):
        if self.isEmpty():
            return -1
        return self.queue[-1]
         
        

q = myQueue(3)

print(q.isEmpty())   # True

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.getFront())  # 10
print(q.getRear())   # 30

print(q.dequeue())   # 10

print(q.getFront())  # 20
print(q.getRear())   # 30

print(q.isEmpty())   # False
print(q.isFull())    # False