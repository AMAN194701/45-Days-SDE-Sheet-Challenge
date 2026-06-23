# Kth largest/smallest element in an array
# Problem Statement: Given an array nums, return the kth largest element in the array.
# Example 1:
# Input: nums = [1, 2, 3, 4, 5], k = 2  
# Output: 4  
# Explanation: The 2nd largest number in the list [1, 2, 3, 4, 5] is 4.

# --------------------------------------------------
# Brute force approach 
# TC - O(n log n) - sorting 
# SC - O(1)
# --------------------------------------------------
import heapq
class Solution:
    def kth_largest_brute(self, nums,k):
        n= len(nums)
        nums.sort()
        return nums[n-k]
    


        # Optimal Approach
    def kth_largest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            # Keep only k elements in the heap
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]

nums = [1, 2, 3, 4, 5]
k = 2
q1 = Solution()
print("Brute Force Answer :", q1.kth_largest_brute(nums.copy(), k))
print("Optimal Answer     :", q1.kth_largest(nums, k))