class Solution:
    def partition(self, s: str) -> list[list[str]]:
        ans = []
        # checking if substring is palindrome
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start, path):
            # reached end of string
            if start == len(s):
                ans.append(path[:])
                return

            # trying every possible partition and continue if it's palindrome
            for end in range(start, len(s)):
                if isPalindrome(start, end):

                    path.append(s[start:end + 1])  # choose
                    backtrack(end + 1, path)       # recurse
                    path.pop()                     # backtrack

        backtrack(0, [])
        return ans
        