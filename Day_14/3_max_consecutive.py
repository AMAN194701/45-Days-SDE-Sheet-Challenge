# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Input: nums = [1,1,0,1,1,1]
# Output: 3
# Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

# --------------------------------------------------
# Max Consecutive Ones 
# TC : O(n)
# SC : O(1)
# --------------------------------------------------
class Solution:
    def findMaxConsecutiveOnes(self, nums):

        max_count = 0
        count = 0

        # Traverse the array
        for num in nums:

            # Increase streak of 1's
            if num == 1:
                count += 1

            # Reset streak when 0 is found
            else:
                count = 0

            # Update maximum streak
            max_count = max(count, max_count)

        return max_count