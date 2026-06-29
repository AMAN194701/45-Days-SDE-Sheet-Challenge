# Stock span problem

# Problem Statement: Given an array arr of size n, where each element arr[i] represents the stock price on day i. Calculate the span of stock prices for each day.

# The span Sᵢ for a specific day i is defined as the maximum number of consecutive previous days (including the current day) for which the stock price was less than or equal to the price on day i.
# Example 1:
# Input: n = 7, arr = [120, 100, 60, 80, 90, 110, 115]
# Output: 1 1 1 2 3 5 6


# --------------------------------------------------
# Brute Force Approach 
# TC : O(n^2)
# SC : O(n)
# --------------------------------------------------
class Solution:
    def brute_stock_span(self, prices):
        span =[]
        
        # Traverse each day 
        for i in range(len(prices)):
            count=0
            # move backward and check if <= previous then +1 count else break
            for j in range(i,-1,-1):
                if prices[j]<=prices[i]:
                    count+=1
                else :
                    break 
            # append the count 
            span.append(count)
        
        return span

sol = Solution()

print(sol.brute_stock_span([100, 80, 60, 70, 60, 75, 85]))


# --------------------------------------------------
# Optimal Approach 
# TC : O(n^2)
# SC : O(n)
# --------------------------------------------------
class solution2:
    def stock_span(slef, prices):
        span=[0]*len(prices)
        stack= [ ]
        for i in range(len(prices)):
            while stack and prices(stack[-1]<=prices[i]):
                stack.pop()
            
            if not stack :
                span[i]= i +1
            else:
                span[i]= i - stack[-1]

            stack.append(i)
            
        return span
