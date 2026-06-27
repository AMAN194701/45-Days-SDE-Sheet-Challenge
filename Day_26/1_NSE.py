# Next Smaller Element
# Problem Statement: Given an array of integers arr, your task is to find the Next Smaller Element (NSE) for every element in the array.
# The Next Smaller Element for an element x is defined as the first element to the right of x that is smaller than x.
# If there is no smaller element to the right, then the NSE is -1.

# Example 1:
# Input: arr = [4, 8, 5, 2, 25]
# Output: [2, 5, 2, -1, -1]


# --------------------------------------------------
# Brute force approach 
# TC : O(n^2)
# SC : O(n)
# --------------------------------------------------
class solution():
    def nse(self, nums):
        n = len(nums)
        ans = [-1]*n
        for i in range(n):
            for j in range(i+1,n):
                if nums[j]<nums[i]:
                    ans[i]= nums[j]
                    break 
        return ans 

q1=solution()
print(q1.nse([4,8,5,2,25])) 
print("-"*50)

# --------------------------------------------------
# Optimal approach 
# TC : O(n)
# SC : O(n)
# --------------------------------------------------
class solution():
    def nse(self, nums):
        n = len(nums)
        stack = [] # mono increasing stack 
        ans= [-1]*n # store the final ans 

        # Traverse from right to left 
        for i in range(n-1,-1,-1): 
            # Remove all elements greater than or equal to current
            while stack and stack[-1] >= nums[i]:
                stack.pop()
            
            # If stack is not empty, the top is the Next Smaller Element.          
            if stack:
                ans[i] = stack[-1]
            # push the curr element to stack 
            stack.append(nums[i])
        return ans 

q1=solution()
print(q1.nse([4,8,5,2,25])) 
print("-"*50)