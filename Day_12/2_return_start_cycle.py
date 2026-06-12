# Problem Statement: Given the head of a linked list that may contain a cycle, return the starting point of that cycle. If there is no cycle in the linked list return null.

# Input: LL: 1  2  3  4  5
# Output: 3
# Explanation: This linked list contains a loop of size 3 starting at node with value 3

# --------------------------------------------------
# Brute Force Approach
# TC : O(n) - each node is visited once
# SC : O(n) - set stores visited nodes
# --------------------------------------------------

def check_cycle(head):
    visited = set()
    temp = head 
    while temp :

        # Same node encountered again => cycle starts here
        if temp in visited:
            return temp 
        
        visited.add(temp)
        temp = temp.next 

    return None


# --------------------------------------------------
# Optimal Approach 
# TC : O(n) - loop
# SC : O(1)
# --------------------------------------------------
def check_cycle(head):
    slow = head 
    fast = head 

    # Check if cycle exixt
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        
        # Meeting point
        if slow == fast :
            entry = head 

            # moving both one step and a time 
            while entry != slow :
                entry = entry.next 
                slow = slow.next 

            return entry 
    
    return None 