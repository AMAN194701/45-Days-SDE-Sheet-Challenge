# --------------------------------------------------
# Brute Force 
# TC :
# SC :
# --------------------------------------------------

class solution:
    def mid_value(self, head):
        curr= head 
        count= 0 
        while curr:
            count+=1
            curr= curr.next 
        mid= count//2 
        curr= head 
        for _ in range(curr):
            curr=curr.next
        return curr 
    

# --------------------------------------------------
# Optimal approach 
# TC :
# SC :
# --------------------------------------------------
class solution:
    def mid_value(self, head):
        slow  = head 
        fast = head 
        while fast and fast.next :
            slow = slow.next
            fast= fast.next.next
        return slow