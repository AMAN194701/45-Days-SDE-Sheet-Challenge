# Problem Statement: Given a linked list and an integer N, the task is to delete the Nth node from the end of the linked list and print the updated linked list.

# Input:  5->1->2, N=2
# Output: 5->2
# Explanation: The 2nd node from the end of the linked list is 1. Therefore, we get this result after removing 1 from the linked list.

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Optimal approach 
# TC : O(2n) -> O(n) - (two traversals — first to count length, then to reach target)
# SC : O(1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# class to assign the value and position 
class give_value :
    def __init__(self, value):
        self.value= value 
        self.next = None

class Solution:
    def remove_node(self,head,n):
        temp= head 
        length= 0 
        
        # counting the length
        while temp:
            length+=1
            temp = temp.next 
        
        # counting the position which we want to remove from the head 
        position= length - n + 1 

        # if position is 1 (head) then return the head.next
        if position == 1 :
            return head.next 
        
        # if not then take ur temp pointer one step behind the nth position which we want to remove
        # but first reset ur temp pointer 
        temp = head 

        # We are substracting 2 position since temp is already at head 
        for _ in range(position-2): 
            temp= temp.next
            
        # break the connection and point to its next value
        temp.next = temp.next.next 

        return head 

def printNum(head):
    while head :
        print(head.value , end = " ")
        head = head.next


head = give_value(1)
head.next = give_value(2)
head.next.next = give_value(3)
head.next.next.next = give_value(4)
head.next.next.next.next = give_value(5)

result = Solution()
head = result.remove_node(head,2)
printNum(head)
print()


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Optimal approach  (single traversal using two pointers, avoids recalculating length or restarting from head)
# TC : O(n)
# SC : O(1)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
class give_value:
    def __init__(self, value):
        self.value =value 
        self.next = None 
class Solution :
    def rm_node(self, head, n):
         # create a fast and slow pointer both pointing to head 
        slow = head 
        fast = head 
        # create a gap of n steps first for fast pointer, and then move both poniter by one step 
        for _ in range(n ):
            fast = fast.next 
        
        if fast is None :
            return head.next 
        # moving both the pointers by 1 step
        while fast.next:
            fast= fast.next
            slow = slow.next  
        # when fast pointer reaches the end then slow is exctly one node behind which we want to remove, so break the connection and form the new one 
        slow.next = slow.next.next 
        
        return head 
    
def printNum(head):
    while head :
        print(head.value, end=" ")
        head = head.next 

head= give_value(1)
head.next= give_value(3)
head.next.next= give_value(7)
head.next.next.next= give_value(2)
head.next.next.next.next= give_value(5)
head.next.next.next.next.next= give_value(9)

result  = Solution()
head= result.rm_node(head,4 )
printNum(head)

