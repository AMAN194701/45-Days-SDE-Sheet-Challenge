class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1, n + 1)]
        # 0-based indexing
        k -= 1  
        ans = ""

        while n:
            # block size
            fact = factorial(n - 1)  
            # pick block
            idx = k // fact          
            ans += nums[idx]
            nums.pop(idx)

            # remaining position
            k %= fact                
            n -= 1

        return ans
        