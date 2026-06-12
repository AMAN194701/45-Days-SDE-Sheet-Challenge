# --------------------------------------------------
# Brute force approach 
# TC : O(m * n) traversing vertically and hortizontally
# SC : O(n)    - in worst case all the values might be added in sort 
# --------------------------------------------------

def flatten(head):
    temp = head 
    values = []
    while temp :
        down = temp 
        while down:
            values.add(temp.val)
            down = down.bottom 
        temp = temp.next 
    values.sort()


        