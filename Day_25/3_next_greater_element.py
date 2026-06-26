class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        nextGreater = {}

        # Process nums2 from right to left
        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()

            if stack:
                nextGreater[num] = stack[-1]
            else:
                nextGreater[num] = -1
            stack.append(num)

        # Build answer for nums1
        ans = []
        for num in nums1:
            ans.append(nextGreater[num])
        return ans
        