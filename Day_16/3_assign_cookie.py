class Solution:
    def assign_cookies(self, g, s):
        g.sort()
        s.sort()
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                i += 1
                j += 1
            else:
                j += 1
        return i


sol = Solution()

print(sol.assign_cookies([1, 2, 3], [1, 1]))
print(sol.assign_cookies([1, 2], [1, 2, 3]))
print(sol.assign_cookies([1, 2, 2, 3], [1, 2, 2]))