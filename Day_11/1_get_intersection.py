# --------------------------------------------------
# Brute Forece approach 
# TC : O(m * n) - nested loop 
# SC : O(1)
# --------------------------------------------------
def get_intersection(headA, headB):
    tempA= headA 
    while tempA:
        tempB= headB 
        while tempB:
            if tempA == tempB :
                return tempA 
            tempB = tempB.next 
        tempA = tempA.next 
    return None

# --------------------------------------------------
# better approach   
# TC : O(m + n) - loops 
# SC : O(n).    - for creating visited 
# --------------------------------------------------
def better_intersection(headA, headB):
    tempA = headA 
    visited = set()
    while tempA :
        visited.add(tempA)
        tempA= tempA.next 
    tempB = headB 
    while tempB :
        if tempB in visited :
            return tempB 
        tempB= tempB.next 
    tempA= tempA.next 



# --------------------------------------------------
# Optimal approach   
# TC : O(m + n) - loops 
# SC : O(1)
# --------------------------------------------------
def get_intersection_opt(headA, headB):
    pA = headA
    pB = headB 
    # Continue until both pointers meet (intersection or None)
    while pA != pB: 
        # If pA reaches the end of list A, start traversing list B.
        if pA:
            pA = pA.next 
        else :
            pA =headB

        # if pB reaches to end of list B, start traversing list A
        if pB :
            pB= pB.next 
        else :
            pB= headA
    return pA
