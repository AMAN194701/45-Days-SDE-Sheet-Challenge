# --------------------------------------------------
# Brute Force Approach 
# TC : O(power)
# SC : O(1) 
# --------------------------------------------------
def Solution(number, power):
    if power==0 :
        return 1 
    
    # Handle -ve power
    is_negative= power<0
    power=abs(power)

    ans= 1

    # Calculating final value
    for i in range(power):
        ans*=number 
    if is_negative:
        return 1/ans 
    
    return ans 
print(Solution(2,3))
print(Solution(2,-2))


# --------------------------------------------------
# Optimal Approach 
# TC : O(log n)
# SC : O(log n) 
# --------------------------------------------------
def Opt_power(number , power):
    # Any number raise to O is 1 
    if power==0 :
        return 1
    
    # if number is -ve then we will update the number in exponential form and update the power in -ve
    elif power <0:
        number = 1/number 
        power = -power 

    if power % 2==0 :
        return Opt_power(number*number , power //2)
    return number * Opt_power(number * number, (power-1)//2)
print(Opt_power(2,3))
print(Opt_power(2,-2))