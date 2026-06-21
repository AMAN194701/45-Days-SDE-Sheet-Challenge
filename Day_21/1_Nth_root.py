# Problem Statement: Given two numbers N and M, find the Nth root of M. The nth root of a number M is defined as a number X when raised to the power N equals M. If the 'nth root is not an integer, return -1.
# Input: N = 3, M = 27
# Output: 3
# Explanation: The cube root of 27 is equal to 3.

# --------------------------------------------------
# Brute Force Approach 
# TC : O(m) 
# SC : O(1)
# --------------------------------------------------
def solution(n,m):
    for i in range(1, m+1):
        if i **n ==m :
            return i 
    return -1 

n = 3
m = 27
print(solution(n,m))

# --------------------------------------------------
# Optimal Approach
# TC : O(log m)
# SC : O(1)
# --------------------------------------------------
def opt_solution(n,m):
    if m == 0:
        return 0 
    low = 1
    high = m 
    while low <= high :
        mid = (low + high)//2
        if mid ** n ==m :
            return mid 
        elif mid **n > m :
            high = mid - 1
        else :
            low = mid +1
    return -1

n = 3
m = 64
print(opt_solution(n,m))