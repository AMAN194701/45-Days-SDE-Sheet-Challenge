class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        result = 0 
        for i in range(len(s)-1):
            # compare curr with next 
            if roman[s[i]] < roman[s[i+1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        
        return result + roman[s[-1]]
    
sol = Solution()

test_cases = [
    "III",       # 3
    "IV",        # 4
    "IX",        # 9
    "LVIII",     # 58
    "MCMXCIV",   # 1994
    "XL",        # 40
    "XC",        # 90
    "CD",        # 400
    "CM",        # 900
]

for roman in test_cases:
    print(f"{roman} -> {sol.romanToInt(roman)}")