# Problem Statement: Given an array of integers arr[] and an integer target.
# if sum of any 2 arr == target then return their index postition else return -1,-1

# Eg.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# --------------------------------------------------
# Brute force approach 
# TC : O(n^2) - nested loop 
# SC : O(1)   - Since no extra space is used 
# --------------------------------------------------
def brute_two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j]==target:
                return [i , j] 
    return [-1,-1] 
print(brute_two_sum( [2,3,6,8,6,3,2],4)) 
# --------------------------------------------------
# Optimal Approach - Hashmap
# TC : O(n) - single pass
# SC : O(n) - storing elements in hashmap
# --------------------------------------------------
def optimal_two_sum(nums, target):
    hashmap={}
    for key, value in enumerate(nums):
        result= target - value 
        if result in hashmap :
            return  [hashmap[result],key]
        hashmap[value]=key
print(optimal_two_sum( [2,3,6,8,6,3,2],4)) 

