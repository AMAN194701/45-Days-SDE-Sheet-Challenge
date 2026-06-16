# Fractional Knapsack Problem : Greedy Approach
# Problem Statement: The weight of N items and their corresponding values are given. We have to put these items in a knapsack of weight W such that the total value obtained is maximized.

# Note: We can either take the item as a whole or break it into smaller units.
# Example 1:
# Input:  val = [60, 100, 120], wt = [10, 20, 30], capacity = 50  
# Output:  240.000000 

# Explanation:
# - Take item 0 (w = 10, v = 60)  
# - Take item 1 (w = 20, v = 100)  
# - Take 2⁄3 of item 2 (w = 20, v = 80)  
# Total value = 60 + 100 + 80 = 240
# --------------------------------------------------
# TC : O(n log n) - sorting 
# SC : O(n)       - storing the values
# --------------------------------------------------

def knapsack(weights,value, capacity):
    items= [] 
    # Calculating the value of per unit weight and sort it 
    for i in range(len(weights)):
        ratio= value[i] / weights[i]
        items.append((ratio, value[i], weights[i]))
    items.sort(reverse=True)

    total_value=0
    
    # Traverse the items and check if it can fit then add else value required fraction 
    for ratio, value, weights in items:
        if weights <=capacity :
            total_value += value 
            capacity-= weights 
        else:
            total_value+= capacity*ratio 
            break 
    return total_value 

wt = [10, 20, 30]
value = [60, 100, 120]
capacity = 50

print(knapsack(wt, value, capacity))
