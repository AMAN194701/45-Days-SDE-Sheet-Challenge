# --------------------------------------------------
# Brute Force Approach 
# TC - O(n^2) - loop and 'in'operator 
# SC - O(1)   - no extra space is used
# --------------------------------------------------
def solution(nums):
    nums.sort()
    n= len(nums)
    missing= -1 
    duplicate  = -1

    # Duplicate
    for i in range(n-1):
        if nums[i]==nums[i+1]:
            duplicate=nums[i]
            break

    # Missing 
    for i in range(1,n+1):
        if i not in nums :
            missing= i 
            break
    return [duplicate, missing]

nums= [1,2,2,4]
result= solution(nums)
print(f"Original : {nums}")
print("Sorting_approach: ",result)
print("-"*30)
# --------------------------------------------------
# Using hashmap 
# TC - O(n)   - loop
# SC - O(n)   - Store all the element in freq 
# --------------------------------------------------
def hash_Solution(nums):
    n= len(nums)
    freq={}

    duplicate=-1
    missing=-1
    for num in nums :
        freq[num]= freq.get(num,0)+1

    for i in range(1,n+1):
        if freq.get(i,0)==2:
            duplicate=i 
        elif freq.get(i,0)==0:
            missing=i 
    return [duplicate, missing]
nums= [1,2,2,4]
result= hash_Solution(nums)
print("Hash approach : ", result)
print("-"*30)

# --------------------------------------------------
# Optimal approach  
# TC O(n)   - Looop
# SC O(1)   - No extra space is used
# --------------------------------------------------
def Solution(nums):
    n=len(nums)
    actual_sum=sum(nums)
    expected_sum=n*(n+1)//2

    Actual_sq_sum=sum(num*num for num in nums)
    Expected_sq_sum=n*(n+1)*(2*n+1)//6

    diff= actual_sum - expected_sum 
    sq_diff = Actual_sq_sum - Expected_sq_sum 

    sum_xy= sq_diff//diff 

    duplicate= (diff + sum_xy)//2 
    missing= duplicate -diff 

    return [duplicate, missing]
nums= [1,2,2,4]
result= Solution(nums)
print("Optimal result :",result)
print("-"*30)

