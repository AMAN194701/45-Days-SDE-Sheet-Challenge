# Problem Statement: Given an array of integers A and an integer B. 
# Find the total number of subarrays having bitwise XOR of all elements equal to k.
# Input: A = [4, 2, 2, 6, 4] , k = 6
# Output: 4
# Explanation: The subarrays having XOR of their elements as 6 are
# [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]

# --------------------------------------------------
# Brute Force Approach:
# TC : O(n^2)
# SC : O(1)
# --------------------------------------------------
def xor_Solution(nums,k):
    n =len(nums)
    count=0
    for i in range(n):
        # XOR of currnt subarr
        currnt_xor= 0 
        # Extending the subarr till end
        for j in range(i,n):
            currnt_xor^=nums[j]
            # If XOR becomes equal to k, we found one valid subarray
            if currnt_xor == k :
                count+=1
    return count

nums=[5, 6, 7, 8, 9]
print(xor_Solution(nums,5))

# --------------------------------------------------
# Optimal Approach:
# TC : 
# SC : 
# --------------------------------------------------

# Not getting it properly, will do later on as my understanding improves by doing more and more Question 


