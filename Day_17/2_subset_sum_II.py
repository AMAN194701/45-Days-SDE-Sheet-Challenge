class Solution:
    def subsetsWithDup(self, nums):
        # bring duplicate together
        nums.sort()
        result=[]

        def backtrack(start, subset):

            # store the curr subset
            result.append(subset[:])
            for i in range(start, len(nums)):
                
                # skip duplicate elements at the same level
                if i > start and nums[i]== nums[i-1]:
                    continue 
                
                subset.append(nums[i])
                backtrack(i +1,subset)
                subset.pop()
        
        backtrack(0, [])

        return result
        