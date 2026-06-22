# --------------------------------------------------
# Brute Force Approach
# TC : O(n^2)
# SC : O(1)
# --------------------------------------------------
def solution(arr):
    n = len(arr)
    for i in range(n):
        count = 0 
        for j in range(n):
            if arr[i]==arr[j]:
                count+=1 
        if count > n//2:
            return arr[i] 
    return -1  
print(solution([2, 2, 1, 1, 1, 2, 2]))

# --------------------------------------------------
# Better approach (using hashmap)
# tc O(n) - one pass to build hashmap + one pass to check frequencies 
# sc O(n) - used hashmap to store the count which store upto n element
# --------------------------------------------------
def Solution(arr):
    n = len(arr)
    
    # Hash map to store the count 
    fre={}

    # count the occurance of each element and store it in fre
    for num in arr:
        if num in fre:
            fre[num]+=1
        else :
            fre[num]=1 
    # returning num if count is > n//2 else after checking all return -1
    for num, count in fre.items():
        if count >n//2:
            return num     
    return -1 
        
print(Solution([2, 2, 1, 1, 1, 2, 2]))


# --------------------------------------------------
# Optimal Approach (Boyer Moore Voting Algorithm)
# TC : O(n) - one loop to find candidate, one to verify
# SC : O(1) - only two variables used
# --------------------------------------------------
def Opt_Solution(nums):
    count=0  # Vote Count
    cnt=0    # Candidate
    n=len(nums)
    # Checking each number
    for num in nums :
        # if count is 0 then choose current element as new candidate and update its count
        if count==0:
            cnt=num 
            count=1 
        # if candidate = current element then count +1
        elif cnt==num:
            count+=1 
        # Different element, cancel one vote
        else: 
            count-=1 

    # Since we got the last survivor but it doesnt means it is > n//2, so we verify it here
    if nums.count(cnt) > n//2:
        return cnt 
    # if no majority exists then return -1
    return -1

print(Opt_Solution([2, 2, 1, 1, 1, 2, 2]))
