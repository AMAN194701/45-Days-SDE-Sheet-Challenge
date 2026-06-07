# Problem Statement: Given an array of N integers, your task is to find unique quads that add up to give a target value. In short, you need to return an array of all the unique quadruplets [arr[a], arr[b], arr[c], arr[d]] such that their sum is equal to a given target.
# Example 1:
# Input Format:arr[] = [1,0,-1,0,-2,2], target = 0
# Result: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Explanation:We have to find unique quadruplets from the array such that the sum of those elements is equal to the target sum given that is 0. The result obtained is such that the sum of the quadruplets yields 0.

# --------------------------------------------------
# Brute Force Approach
# TC : O(n^4) - 4 nested loops
# SC : O(n)   - storing unique quadruplets in set
# --------------------------------------------------

def Brute_4sum(nums,target):
    n = len(nums)
    # set to store unique elements
    result=set()
    n = len(nums)
    # pick 4 number
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    # take sum of all these 4 number
                    curnt_sum=nums[i] + nums[j] + nums[k] + nums[l]
                    # check if it is = to target, if so then sort it 
                    if curnt_sum==target:
                        sorted_sum=sorted([nums[i] , nums[j] , nums[k] , nums[l]])

                        # convert it into tuple since set wont accept list and add it in resut
                        result.add(tuple(sorted_sum)) 

    return [list(num) for num in result]



# --------------------------------------------------
# Optimal Force Approach
# TC : O(n^3) - Loop and 2 pointer
# SC : O(1)
# --------------------------------------------------
def Solution(nums,target):
    n= len(nums)
    nums.sort()
    result=[]
    for i in range(n):
        if i > 0 and nums[i]==nums[i-1]:
            continue
        for j in range(i+1,n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            left = j+1
            right= n-1 
            while left < right :
                total_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if total_sum== target :
                    result.append([nums[i],nums[j], nums[left],nums[right]])

                    while left < right and nums[left]== nums[left + 1]:
                        left +=1 
                    while left < right and nums[right]== nums[right-1]:
                        right-=1
                    
                    left+=1
                    right-=1

                elif total_sum <target :
                    left+=1
                else :
                    right -=1 
    return result



# Test Input
nums = [1, 0, -1, 0, -2, 2]
target = 0

print("Brute Force Output:")
print(Brute_4sum(nums, target))

print("\nOptimal Output:")
print(Solution(nums, target))