# --------------------------------------------------
# Brute Force Approach 
# TC : O(n^2) - loops
# SC : O(1) - result can contain max 2 numbers (fixed)
# --------------------------------------------------
# Create a variable to store the result - create a loop & check if it is already present in result if so then skip  
# if not then count its freq and then check  is > then n//3 and append it in result 

def brute_majority(nums):
    n = len(nums)
    result= []

    for num in nums :
        if num  in result:
            continue 

        count =0 
        for el in nums :
            if el == num :
                count+=1
        # Check condition 
        if count >n//3:
            result.append(num)
    return result

print(brute_majority([11, 33, 33, 11, 33, 11]))




# --------------------------------------------------
# Majority Element II — Boyer Moore Voting 
# TC : O(n) - two passes
# SC : O(1) - only 4 const variables have been used
# --------------------------------------------------

def boyer_moore_majority(nums):
    # votes for both candidates
    count1=0
    count2=0

    cnt1=0
    cnt2=0
    n=len(nums)

#   Selecting candidates
    for num in nums :
        # increase the count if cnt matches with current number
        if cnt1==num:
            count1+=1
        elif cnt2==num:
            count2+=1 
        #  if count of any cnt is 0 then make cnt as current number and make its count as 1 
        elif count1==0:
            cnt1=num 
            count1=1
        elif count2==0:
            cnt2=num 
            count2=1 
        # if current number is different then cancle one count from them
        else :
            count1-=1
            count2-=1 
    
    # Verification check if they appears more than n//3 

    result=[]
    if nums.count(cnt1) >n//3:
        result.append(cnt1)
    if cnt2 != cnt1 and nums.count(cnt2)> n//3:
        result.append(cnt2)

    return result

print(boyer_moore_majority([11, 33, 33, 11, 33, 11]))
