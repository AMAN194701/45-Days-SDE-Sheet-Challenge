# --------------------------------------------------
# Brute Force Approach :
# TC : O(n)
# SC : O(1)
# --------------------------------------------------
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0 
        n = len(s)
        num = 0 
        sign = 1

        # check spaces 
        while i < n and s[i] == " ":
            i +=1 
        
        # handle sign 
        if i < n :
            if s[i] == "-":
                sign = -1
                i+=1 
            elif s[i]== "+" :
                i+=1 

        # Read digits 
        while i <n and s[i].isdigit():
            digit = int(s[i])
            num = num *10 +digit 
            i+=1
        
        # apply sign 
        num *=sign 

        MIN_INT = -(2**31)
        MAX_INT = 2**31-1 

        # check range
        if num < MIN_INT:
            return MIN_INT
        elif num > MAX_INT :
            return MAX_INT
        return num
        