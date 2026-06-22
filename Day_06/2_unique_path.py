# --------------------------------------------------
# Brute Force Approach
# TC : O(2^(i*j)) - two recursive calls at each cell
# SC : O(i+j)     - recursion call stack depth
# --------------------------------------------------
def Solution(i,j):
    # reach start
    if i==0 and  j==0:
        return 1
    # out of grid 
    if i<0 or j <0 :
        return 0

    up = Solution(i-1,j)
    left = Solution(i, j-1)

    return up+ left 
print(Solution(2,1)) 

# --------------------------------------------------
# Memoization Approach
# TC : O(m*n)       - each cell calculated only once
# SC : O(m*n)       - dp table
#    + O(m+n)       - recursion 
# --------------------------------------------------
def memo(m,n,dp):
    # reach the start 
    if m==0 and n ==0:
        return 1
    
    # out of grid 
    if m<0 or n < 0:
        return 0 
    
    # if already calculated 
    if dp[m][n] != -1 :
        return dp[m][n]
    
    up = memo(m-1,n,dp)
    left=memo(m,n-1,dp)

    dp[m][n]=up+left 

    return dp[m][n]

dp=[[-1 for _ in range(2)] for _ in range(3)]
print(memo(2,1,dp))


