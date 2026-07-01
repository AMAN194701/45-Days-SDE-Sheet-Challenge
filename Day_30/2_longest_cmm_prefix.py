# --------------------------------------------------
# TC : O(m + n)
# SC : O(1)
# --------------------------------------------------
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # assume 1st str as a common 
        prefix = strs[0]

        # compare prefix with remaning 
        for word in strs[1:]:
            i=0 
            
            # common prefix len 
            while i < len(prefix) and i < len(word) and prefix[i]== word[i]:
                i+=1

            # Shrink it to the match part 
            prefix = prefix[:i]
            
            # if no common prefix exist 
            if not prefix :
                return ""
        return prefix 


             