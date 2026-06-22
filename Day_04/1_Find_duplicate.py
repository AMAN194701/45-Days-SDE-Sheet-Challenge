# Find the duplicate in an array of N+1 integers
# Problem Statement: Given an array of N + 1 size, where each element is between 1 and N. 
# Assuming there is only one duplicate number, your task is to find the duplicate number.
# --------------------------------------------------
# Brute force Approach 
# TC - O(n^2) 
# SC - O(n)
# --------------------------------------------------
def Solution(arr):
    duplicate=[]
    n= len(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                duplicate.append(arr[i])
    return duplicate
arr=[1,2,3,4,5,1,4]
result= Solution(arr)
print(f"Original : {arr}")
print(f"The duplicate elements are : {result} ")
print("-"*30)


            # OR
# --------------------------------------------------
# Sorting Approach
# TC - O(n log n) - Sorting
# SC - O(1)       - Since no extra space is used 
# --------------------------------------------------

def solution(arr):
    arr.sort()
    n=len(arr)
    for i in range(n-1):
        if arr[i]==arr[i+1]:
            return arr[i]
               
arr=[3,3,3,3]
result= solution(arr)
print(f"Original : {arr}")
print(f"The duplicate elements are : {result} ")
print("-"*30)
        

# ------------------------------------------------------------
# Using Hashset approach
# TC - O(n) - since loop
# SC - O(n) -
# ------------------------------------------------------------
def Solution(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return num 
        else:
            seen.add(num)

nums=[1,2,4,2,1]
result=Solution(nums)
print(result)


# ------------------------------------------------------------
# Using Optimal approach (Floyd's Cycle Detection)
# TC - O(n) - Loop
# Sc - O(1) - No extra space is used 
# ------------------------------------------------------------
def Solution(nums):
    # Pointers
    slow = nums[0]
    fast = nums[0]

    # Move slow by 1 and fast by 2 index value until duplicate found
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if slow==fast:
            break 
    
    # reset slow to find where duplicate loop starts
    slow=nums[0]
    while slow!=fast :
        slow=nums[slow]
        fast=nums[fast]
    
    # return duplicate
    return slow
