# --------------------------------------------------
# optimal approach
# TC : O(n) - loops for calculating len and new tail
# SC : O(1)
# --------------------------------------------------


def rotateRight(head, k: int):
    while not head or not head.next or k==0:
        return head 
    
    len = 1  # started with 1 becz temp is already at the first position
    temp = head 

    while temp.next :
        temp = temp.next 
        len+=1    
    
    k = k % len #avoid unecessary roatation 

    if k ==0 :
        return head 

    # make it circular
    temp.next = head

    # find the new tail
    new_tail = head
    for _ in range(len-k-1):
        new_tail = new_tail.next 

    # find the new head and point new tail to next 
    new_head = new_tail.next 
    new_tail.next = None 
    
    # return new head 
    return new_head