# --------------------------------------------------
# Remove Duplicates from Sorted Array (LC 26)
# Optimal Approach : Two Pointers
# TC : O(n)
# SC : O(1)
# --------------------------------------------------
class Solution:
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        
        # Points to last unique element 
        i=0 

        # Traverse the array
        for j in range(1,len(nums)):
            # if new unique element found
            if nums[i]!= nums[j]:
                i+=1
                nums[i]=nums[j]

        return i+1