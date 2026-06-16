# --------------------------------------------------
# TC :  O(n log n) - sorting 
# SC :  O(n)
# --------------------------------------------------

def min_no_of_coin(coins, amount):
    coins.sort(reverse =True)
    result= []
    for coin in coins:
        count = amount // coin 
        if count> 0 :
            result.extend([coin] *count)
            amount %=coin 
    return result

coins = [1, 2, 5, 10, 20, 50, 100, 200, 500]
amount = 2753
print(min_no_of_coin(coins,amount))


# --------------------------------------------------
# TC :
# SC : 
# --------------------------------------------------
class Solution:
    def coin_change(self, coins, amount):
        dp={}
        return self.helper(coins, amount,dp )
    
    def helper(self, coins, rest, dp):
        if rest==0 :
            return 0 
        if rest < 0 :
            return -1 

        if rest in dp :
            return dp[rest]
    
        minn = float('inf')

        for coin in coins:
            res = min(coins, rest - coin, dp)
        
            if res >= 0 and res < min :
                mini = 1+ res 
            
        dp[rest] = -1 if mini == float('inf') else mini
        return dp[rest]

        