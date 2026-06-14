# --------------------------------------------------
# Optimal approach 
# TC : O(n)  - loop
# SC : O(1)  - Auxiliary Space
# --------------------------------------------------
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList( head):

    if not head:
        return None

    # Insert copied nodes
    temp = head

    while temp:
        nxt = temp.next
        copy = Node(temp.val)

        temp.next = copy
        copy.next = nxt
        temp = nxt

    # Assign random pointers
    temp = head

    while temp:
        if temp.random:
            temp.next.random = temp.random.next

        temp = temp.next.next

    # Separate the lists
    temp = head
    dummy = Node(-1)
    copy_curr = dummy

    while temp:
        copy = temp.next

        temp.next = copy.next
        temp = temp.next

        copy_curr.next = copy
        copy_curr = copy

    return dummy.next



