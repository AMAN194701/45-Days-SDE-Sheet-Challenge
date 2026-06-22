# --------------------------------------------------
# Brute force 
# TC : O(n^2) - nested loop 
# SC : O(1)   - no extra space is used 
# --------------------------------------------------
def Brute_sum(nums):
    max_len =0  # Because there may be no subarray whose sum is 0.
    n=len(nums)
    # Starts from the first number 
    for i in range(n):
        curr_sum=0
        # check if the sum of next number sum is 0 
        for j in range(i,n):
            curr_sum +=nums[j]
            # if sum is zero then compare its length with previous sum len
            if curr_sum ==0:
                max_len=max(max_len, j-i+1)
    return max_len

arr=[9, -3, 3, -1, 6, -5]
print(Brute_sum(arr))


# --------------------------------------------------
# Optimal approach using Hashmap
# TC : O(n)   - single loop 
# SC : O(1)   - no extra space is used 
# --------------------------------------------------

def longest_sum(nums):
    prefix_sum=0        # Stores the sum 
    hashmap={}          # Stores the occurance of the first come
    max_len=0
    n=len(nums)     
    # Traverse Through arr 
    for i in range(n):
        # update the current sum
        prefix_sum +=nums[i]

        if prefix_sum==0:
            max_len =i+1
        if prefix_sum in hashmap:
            max_len= max(max_len, i - hashmap[prefix_sum])
        else :
            hashmap[prefix_sum]=i 
        
    return max_len

arr=[9, -3, 3, -1, 6, -5]
print(longest_sum(arr))