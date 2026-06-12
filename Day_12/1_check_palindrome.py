# --------------------------------------------------
# Brute Force Approach 
# TC : O(n) - loop
# SC : O(n) - list creation
# --------------------------------------------------

def is_palindrome(head):
    # since it is a singly ll so and we cant go backward,
    # so we store the node value in arr 
    arr=[]
    temp= head 

    # Traverse the ll and store the values 
    while temp:
        arr.append(temp.val)
        temp= temp.next 
    
    # start from the both the ends of the ll  
    left = 0 
    right = len(arr) -1
    
    # compare both the values from the end 
    while left < right :
        if arr[left] != arr[right]:
            return False 
        left +=1 
        right -=1 
    return True 


# --------------------------------------------------
# Optimal Approach 
# TC : O(n)
# SC : O(1)
# --------------------------------------------------

def check_palindrome(head):
    slow = head 
    fast = head 
    # Find the mid
    while fast.next and fast.next.next :
        slow= slow.next 
        fast= fast.next.next 
    
    # reverse the sec half 
    prev= None 
    curr = slow.next 
    while curr :
        next_node= curr.next 
        curr.next = prev 
        prev = curr 
        curr= next_node

    # Compare the values 
    first = head 
    sec = prev 
    while sec :
        if first.val != sec.val :
            return False 
        first= first.next 
        sec = sec.next 
    return True  
    

    

