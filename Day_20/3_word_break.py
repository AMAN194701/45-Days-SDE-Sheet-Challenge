class Solution:
    def solve(self, index, s, wordSet, path, ans):
        # Entire string has been used
        if index == len(s):
            ans.append(" ".join(path))
            return
        # try every possible substring starting from index
        for end in range(index + 1, len(s) + 1):
            word = s[index:end]
            # If word exists in dictionary
            if word in wordSet:
                # Choose
                path.append(word)
                # Explore remaining string
                self.solve(end, s, wordSet, path, ans)
                # Backtrack
                path.pop()

    def wordBreak(self, s, wordDict):
        ans = []
        wordSet = set(wordDict)
        self.solve(0, s, wordSet, [], ans)
        return ans
s = "catsanddog"

wordDict = [
    "cat",
    "cats",
    "and",
    "sand",
    "dog"
]

obj = Solution()

print(obj.wordBreak(s, wordDict))