# Brute Force Approach

class BruteForceSolution:
    # Check if the string is palindrome
    def isPalindrome(self, word):
        left = 0
        right = len(word) - 1

        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1

        return True

    # Generate all substrings and check for palindrome
    def longestPalindrome(self, s: str) -> str:
        max_len = 0
        result = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                substring = s[i:j + 1]

                if self.isPalindrome(substring):
                    if len(substring) > max_len:
                        max_len = len(substring)
                        result = substring

        return result


# Optimal Approach: Expand Around Center

class OptimalSolution:
    def expand(self, s, left, right):
        while left >= 0 and right < len(s):
            if s[left] != s[right]:
                break

            curr_len = right - left + 1

            if curr_len > self.max_len:
                self.max_len = curr_len
                self.start = left

            left -= 1
            right += 1

    def longest_palindrome(self, s):
        if not s:
            return ""

        self.start = 0
        self.max_len = 1

        for i in range(len(s)):
            # Odd length palindrome
            self.expand(s, i, i)

            # Even length palindrome
            self.expand(s, i, i + 1)

        return s[self.start:self.start + self.max_len]


# -------------------- Testing --------------------

tests = [
    "babad",
    "cbbd",
    "abba",
    "racecar",
    "banana",
    "abcd",
    "a",
    ""
]

print("Brute Force")
print("=" * 30)
brute = BruteForceSolution()

for s in tests:
    print(f"Input : {s!r}")
    print(f"Output: {brute.longestPalindrome(s)}")
    print("-" * 30)

print("\nOptimal")
print("=" * 30)
optimal = OptimalSolution()

for s in tests:
    print(f"Input : {s!r}")
    print(f"Output: {optimal.longest_palindrome(s)}")
    print("-" * 30)