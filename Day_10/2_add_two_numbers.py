# Problem Statement: Add two numbers represented as Linked Lists.
# Example 1:
# Input: num1 = 243, num2 = 564
# Output:sum = 807; L = [7,0,8]

# --------------------------------------------------
# Add Two Numbers
# TC : O(max(n, m))
# SC : O(max(n, m))
# --------------------------------------------------
class ListNode :
    def __init__(self, value):
        self.value= value 
        self.next = None 

class Solution:
    def add_two_num(self, l1,l2):
         # creating a dummy variable at starting point (empty list handling)
        dummy = ListNode(0)
        temp= dummy # temp variable, initially pointing to dummy
        carry =0 
        
        # Run while l1 or l2 still pointing to node or carry is still non zero
        while l1 or l2 or carry :
            total = carry 
            
            # add l1 and l2 values and increase their pointer
            if l1 :
                total += l1.val
                l1 = l1.next 
            
            if l2 :
                total += l2.val
                l2 = l2.next 

            # count digit value and carry 
            digit = total % 10 
            carry = total // 10 
            
            # create a new node 
            temp.next = ListNode(digit)

            # move the temp variable in order to add next value 
            temp = temp.next 
        
        # dummy points to ListNode(0), so return dummy.next which is the actual head of result
        return dummy.next 

