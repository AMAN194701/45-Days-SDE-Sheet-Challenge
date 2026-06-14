# Problem Statement: Given an array of non-negative integers representation elevation of ground. Your task is to find the water that can be trapped after rain .

# Input : height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output : 6
# Explanation : Water is trapped in the dips between bars. The total trapped water units add up to 6 (1+1+2+1+1).

# --------------------------------------------------
# Optimal Approach 
# TC : O(n)
# SC : O(1)
# --------------------------------------------------
class Solution:
    def trap(self, height):
        left = 0
        right = len(height) - 1

        max_left = 0
        max_right = 0

        total_water = 0

        while left <= right:

            # Left side determines trapped water
            if height[left] <= height[right]:

                # update left maximum
                if height[left] >= max_left:
                    max_left = height[left]

                # water trapped at current index
                else:
                    total_water += max_left - height[left]

                left += 1

            # right side determines trapped water
            else:

                # update right maximum
                if height[right] >= max_right:
                    max_right = height[right]

                # water trapped at current index
                else:
                    total_water += max_right - height[right]

                right -= 1

        return total_water