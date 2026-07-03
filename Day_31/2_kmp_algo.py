# --------------------------------------------------
# TC : O(n³)
# SC : O(n)
# --------------------------------------------------
class solution:
    def build_lps(self, pattern):
        n = len(pattern)
        lps = [0]*n
        for i in range(n):
            substring  =pattern[: i+1]

            for j in range(len(substring)-1,0,-1):
                prefix = substring[:j]
                suffix = substring[-j:]
                if prefix == suffix:
                    lps[i] = j
                    break   
        return lps
    
    def KMP(self, text, pattern):

        lps = self.build_lps(pattern)
        result= []
        i= j = 0
        while i< len(text):
            if text[i] ==pattern[j]:
                i += 1
                j += 1

            if j== len(pattern):
                result.append(i - j)
                j = lps[j - 1]

            elif i< len(text) and text[i] != pattern[j]:
                if j != 0:
                    j = lps[j -1]
                else:
                    i +=1
        return result

a = solution()
text = "ababcababcabc"
pattern = "abc"

print(a.KMP(text, pattern))