class Solution:
    def combinationSum(self, candidates, target):
        result = []
        def solve(index, target, path):
            # Found a valid combination
            if target == 0:
                result.append(path[:])
                return
            # Array finished
            if index == len(candidates):
                return
            # Take current number (can be reused)
            if candidates[index] <= target:
                path.append(candidates[index])
                solve(
                    index,
                    target - candidates[index],
                    path
                )
                path.pop()
            # Skip current number
            solve(index + 1, target, path)
        solve(0, target, [])
        return result
    

obj = Solution()
print(obj.combinationSum([2,3,6,7], 7))
print(obj.combinationSum([2], 1))