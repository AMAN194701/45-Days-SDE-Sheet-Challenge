from collections import deque
class Solution:
    def maxSlidingWindow(self, nums:list[int], k: int) -> list[int]:
        dq = deque()
        ans = []

        for i in range(len(nums)):
            # remove indices outside the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove smaller element
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            # add current index
            dq.append(i)

            # store max
            if i >= k - 1:
                ans.append(nums[dq[0]])

        return ans
        