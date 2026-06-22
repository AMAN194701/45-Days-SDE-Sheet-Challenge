# --------------------------------------------------
# Brute Force Approach
# TC : O(n^3)
# SC : O(1)
# --------------------------------------------------
# helper function to check if next consecutive number is present in list or not
def linear_Search(nums,num):
    n= len(nums)
    for i in range(n):
        if nums[i]==num:
            return True
    return False

def brute_longest_consecutive(nums):
    # if len of arr is 0 then return 0
    n = len(nums)
    if n==0:
        return 0
    # Since a single number could be higest 
    longest=1
    for i in range(n):
        x=nums[i]
        count=1
        # Search for the number 
        while linear_Search(nums,x+1):
            count+=1
            x+=1 
        longest=max(longest,count)
    return longest



# --------------------------------------------------
# Optimal Approach - HashSet
# TC : O(n) - loop
# SC : O(n) - storing all elements in set
# --------------------------------------------------
def opt_longest_consecutive(nums):
    n = len(nums)   # len
    if n ==0:        # if len is < 1 then return 0 
        return 0 
    highest=1

    set_form=set(nums)   # converting list into set because it take O(1) for searching 
    
    # Checking the start and then increasing its count by +1 and checking if next element is prsnt then +1 count
    for num in set_form:    
        if num-1 not in set_form:
            count=1
            currnt=num 

            while currnt+1 in set_form :
                count+=1
                currnt+=1
            # highest would be the max of current count and previous highest
            highest= max(highest, count)
    return highest

    
numbers=[100, 4, 200, 1, 3, 2]
result1=brute_longest_consecutive(numbers)
result2=opt_longest_consecutive(numbers)
print(result1)
print(result2)