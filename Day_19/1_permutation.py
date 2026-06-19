def solution(nums):
    result= []

    if len(nums)==0:
        return [nums.copy()]
    
    for i in range(len(nums)):
        # remove the current element from the list 
        n= nums.pop(0)

        # get the permutations of the remaining elements 
        perm= solution(nums)