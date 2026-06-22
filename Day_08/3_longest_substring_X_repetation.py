# Problem Statement: Given a string, S. Find the length of the longest substring without repeating characters.
# --------------------------------------------------
# Brute Force approach 
# TC : O(n^2) - nested loop 
# SC : O(1)   - no extra space is used
# --------------------------------------------------

def Solution(c):
    n=len(c)
    max_len=0
    for i in range(n):
        seen=set()              # Stores unique characters 
        for j in range(i,n):
            if c[j] in seen:    # If duplicate found then break if not then add in seen and update the max_len
                break 
            seen.add(c[j])
            max_len=max(max_len,j-i+1)
    return max_len 

s="abcddabac"
print(Solution(s))

# --------------------------------------------------
# Optimal Approach - Sliding Window
# TC : O(n) - each element enters and leaves window once
# SC : O(n) - storing characters in set
# --------------------------------------------------

def opt_solution(s):
    max_len=0 # store valid max len 
    n = len(s)
    left = 0 
    seen=set() # Stores the unique charaters
    # increase the widow size
    for right in range(n):
        # if duplicate found , remove the numbers from left untile duplicate number is removed
        while s[right] in seen:
            seen.remove(s[left]) # removing number from left 
            left+=1
        # add currnt element in window if not in set
        seen.add(s[right])
        # update the max_length 
        max_len= max(max_len, right-left+1)
    return max_len
s="abcddabac"
print(opt_solution(s))
