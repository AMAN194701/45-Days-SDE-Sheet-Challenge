# Search Element in a Rotated Sorted Array
# Problem Statement: Given an integer array nums, sorted in ascending order 
# (with distinct values) and a target value k. The array is rotated at some pivot 
# point that is unknown. Find the index at which k is present and if k is not present return -1.

# Input:nums = [4, 5, 6, 7, 0, 1, 2], k = 0
# Output :4
# Explanation : Here, the target is 0. We can see that 0 is present in the given rotated sorted array, nums. Thus, we get output as 4, which is the index at which 0 is present in the array.
 
# --------------------------------------------------
# Brute Force Approach
# TC : O(n)
# Sc : O(1)
# --------------------------------------------------
def solution(nums, k):
    for i in range(len(nums)):
        if nums[i] == k :
            return i
    return -1
nums = [4, 5, 6, 7, 0, 1, 2]
k = 0       
print(solution(nums, k))


# --------------------------------------------------
# Optimal Approach
# TC : O(log n)
# Sc : O(1)
# --------------------------------------------------
def opt_solution(nums,k):
    low= 0 
    high= len(nums)-1
    while low <= high :
        mid= (low+high)//2
        if nums[mid]==k :
            return mid 
        
        # Check if left half is sorted
        # If target lies in the left sorted half, search left
        if nums[low]<= nums[mid]:
            if nums[low] <= k < nums[mid]:
                high = mid- 1
            else :
                low = mid +1
        # otherwise right half must be sorted so check for target
        else :
            if nums[mid] < k <= nums[high]:
                low = mid +1
            else :
                high = mid -1

    # if not present in both return -1
    return -1

nums = [4, 5, 6, 7, 0, 1, 2]
k = 0
print(opt_solution(nums, k))