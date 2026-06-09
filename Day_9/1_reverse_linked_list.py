# --------------------------------------------------
# Brute force approach 
# TC : O(n) - loop 
# SC : O(n) - values are getting stored in stack 
# --------------------------------------------------
class listNode:
    # what ever vaues we will give in this it will store the value and create pointer 
    def __init__(self, val=0 , next =None):
        self.val= val 
        self.next= next 
class Solution :
    def reversedlist(self,head):
        # creting empty stack 
        stack=[]

        # temp head for appending the values in stack 
        temp = head 

        # while temp is giving the value we will append that value in stack and move the pointer to next
        while temp:
            stack.append(temp.val)
            temp= temp.next 
        
        # reset the temp to head for overwriting the values from stack 
        temp = head 
        
        # Since stack in LIFO so remove the value from stack and assing in it temp.value and move the pointer to next
        while temp :
            temp.val= stack.pop()
            temp= temp.next 

        return head 

def printList(head):
    while head :
        print(head.val, end =" ")
        head= head.next
head= listNode(1)
head.next= listNode(2)
head.next.next = listNode(3)

result = Solution()
head= result.reversedlist(head)
printList(head)
print()



# --------------------------------------------------
# Optimal approach 
# TC : O(n) - single loop 
# SC : O(1)
# --------------------------------------------------
class give_values:
    # what ever vaues we will give in this it will store the value and create pointer 
    def __init__(self,val=0, next= None):
        self.val= val 
        self.next = next 
    
class Solution:
    def reversed_num(self,head):      
        previous = None 
        # curr will point to the current node 
        curr = head
        # raverse until end of the list , reversing each pointer
        while curr:
            # preserve the of next node, if we break it before preserving then we would the other data
            next_node = curr.next 
            # now break the pointer and point it towards the previous 
            curr.next = previous 
            # now shift the previous and curr node 
            previous = curr 
            curr = next_node 
        #  return the previous which would be new head 
        return previous 
def printList(head):
    while head :
        print(head.val, end= " -> " if head.next else " ")
        head= head.next

head= give_values(1)
head.next = give_values(2)
head.next.next =give_values(3)

result= Solution()
head = result.reversed_num(head)
printList(head)
    
        