# Problem Statement: Given an array of N integers. Every number in the array except one appears twice. Find the single number in the array.
# Input : arr[] = {1,1,2,2,3,3,4,5,5,6,6}
# Output: 4
# Explanation: Only the number 4 appears once in the array.

# --------------------------------------------------
# Brute force approach
# TC : O(n)
# SC : O(1)
# --------------------------------------------------


def solution(arr):
    count = 0
    for i in range(0,len(arr)-1,2):
        if arr[i] != arr[i+1]:
            return arr[i]
    return arr[-1] 
arr = [1,1,3,5,5]
print(solution(arr))


# --------------------------------------------------
# Optimal approach (Using Binary Search)
# TC : O(n)
# SC : O(1)
# --------------------------------------------------
def opt_solution(arr):
    n = len(arr)
    # check if only single element is present 
    if n ==1:
        return arr[0]
    
    # first element is single
    if arr[0] != arr[1]:
        return arr[0]
    # Last element is single
    if arr[n-1] != arr[n-2]:
        return arr[n-1]
    
    # Binary search for single element
    low , high = 1 , n-2
    while low <= high :
        mid = (low+high)//2

        # Ans
        if arr[mid] != arr[mid-1] and arr[mid] != arr[mid+1]:
            return arr[mid]
        
        if (mid %2==0  and arr[mid] == arr[mid+1] ) or \
              (mid %2==1  and arr[mid] == arr[mid-1] ): 
            low = mid +1
        else :
            high = mid -1
    return -1   

arr = [1,1,2,2,3,4,4,5,5]

print(opt_solution(arr))