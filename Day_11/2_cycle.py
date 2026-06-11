# Problem Statement: Given a Linked List, determine whether the linked list contains a cycle or not.
# Eg. Input: head = [3,2,0,-4], pos = 1
# Output: true

# --------------------------------------------------
# Brute Force approach
# TC : O(n)
# SC : O(n)
# --------------------------------------------------

def brute_cycle(head):
    temp= head
    # create a empty set 
    visited = set()

    # Same node encountered again => cycle exists
    while temp :
        if temp in visited :
            return True 
        visited.add(temp)
        temp= temp.next



# --------------------------------------------------
# Optimal approach (Floyd's Algorithm)
# TC : O(n)
# SC : O(1)
# --------------------------------------------------
def cycle(head):
    slow = head
    fast = head

    # fast moves 2 step so fast and fast.next must exist 
    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next 

        # Same node visited by both pointers => cycle exists
        if slow == fast :
            return True 
    return False

