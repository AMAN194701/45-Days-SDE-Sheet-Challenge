# Implement Stack using Array

# Problem Statement: Implement a Last-In-First-Out (LIFO) stack using an array. The implemented stack should support the following operations:
#  push, pop, peek, and isEmpty.

# Implement the ArrayStack class:
# void push(int x): Pushes element x onto the stack. int pop(): Removes and returns the top element of the stack. 
# int top(): Returns the top element of the stack without removing it. boolean isEmpty(): Returns true if the stack is empty, false otherwise.


class Solution():
    def __init__(self,n):
        self.stack=[]
        self.capacity = n
    
    # check if stack is full 
    def is_full(self):
        return len(self.stack)== self.capacity
    
    # push the element at the top
    def push(self, value):
        if self.is_full():
            return -1
        self.stack.append(value)
    
    # remove the element from the top 
    def pop(self):
        if self.is_empty():
            return -1
        return self.stack.pop() 
    
    # just show the top most element 
    def peek(self):
        if self.is_empty():
            return -1
        return self.stack[-1]
    
    # check if stack is empty 
    def is_empty(self):
        return len(self.stack)==0


s = Solution(3)

s.push(10)
s.push(20)
s.push(30)

print(s.peek())     

print(s.pop())      
print(s.pop())       

print(s.peek())      