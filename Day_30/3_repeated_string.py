class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeated = a
        count = 1

        while len(repeated)<len(b):
            repeated += a
            count += 1

        # check if b is now a substring
        if b in repeated:
            return count

        # extra repetition to handles overlap cases
        repeated+= a
        count+= 1

        if b in repeated:
            return count

        return -1