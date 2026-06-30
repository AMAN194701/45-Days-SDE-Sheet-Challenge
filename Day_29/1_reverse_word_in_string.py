# Reverse Words in a String
# Problem Statement: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). 
# A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. Return a string with the words in reverse order, concatenated by a single space.

# Examples
# Input: s = "welcome to the jungle"
# Output: "jungle the to welcome"

# --------------------------------------------------
# Brute Force 
# TC : O(n)
# SC : O(n)
# --------------------------------------------------
class solution :
    def rev_str(self,sentence):
        # list to store words 
        words=[]
        
        # store curr word
        word =""

        # Traverse the whole sentence 
        for ch in sentence:
            # if not space then add the char else(space +nt) append the word and reset
            if ch != " ":
                word+=ch
            elif word  :
                words.append(word)
                word =""
        # Add the last word 
        if word :
            words.append(word)
        
        # reverse 
        words.reverse()

        # return 
        return " ".join(words)

sol= solution()
print(sol.rev_str("I love Coding"))



# --------------------------------------------------
# Optimal Approach  
# TC : O(1)
# SC : O(n)
# --------------------------------------------------
class Solution:
    def reverseWords(self, s):
        ans = []
        i = len(s)-1
        
        # skip all extra spaces
        while i >=0 :
            while i >=0 and s[i] ==" ":
                i -=1
            
            # break if no char left 
            if i <0 :
                break 
            
            # mark end of curr word  
            j = i 

            # move to the begning of word 
            while i >= 0 and s[i] !=" ":
                i -=1
            
            # store the word 
            ans.append(s[i+1 : j+1])
        return " ".join(ans)


sol= Solution()
print(sol.reverseWords("I love Coding"))