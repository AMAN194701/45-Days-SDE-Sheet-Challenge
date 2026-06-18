class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()  # sort to handle duplicates
        ans = []
        def backtrack(start, target, path):
            # valid combination found
            if target == 0:
                ans.append(path[:])
                return

            for i in range(start, len(candidates)):
                # skip duplicate numbers at same level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # no need to continue further
                if candidates[i] > target:
                    break

                path.append(candidates[i])  # choose
                # move to next index 
                backtrack(i + 1, target - candidates[i], path)

                path.pop()  # backtrack

        backtrack(0, target, [])
        return ans