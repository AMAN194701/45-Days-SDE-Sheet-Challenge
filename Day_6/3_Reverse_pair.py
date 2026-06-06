# --------------------------------------------------
# Brute force approach 
# TC : O(n^2) - nested loop
# SC : O(1)   - no extra space is used
# --------------------------------------------------
def brute_reverse_pair(nums):
    n = len(nums)
    count= 0 
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] > 2* nums[j]:
                count+=1 
    return count 
print(brute_reverse_pair([1,3,2,3,1]))

# --------------------------------------------------
# Optimal Approach (Merge Sort)
# TC : O(n log n) - merge sort
# SC : O(n)       - extra space for merged array
# --------------------------------------------------

def merge(left, right):
    count=0 
    j=0 
    # count reverse pair using two pointer
    for i in range(len(left)):
        while j < len(right) and left[i] > 2* right[j]:
            j+=1
        count +=j 
    
    result=[]
    i =0 
    j =0 
    while i <len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else :
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result,count 

def merge_sort(arr):
    n = len(arr)

    # base case
    if n <= 1:
        return arr , 0 
    mid = n//2
    left, left_count = merge_sort(arr[:mid])
    right, right_count= merge_sort(arr[mid:])

    merged, s_count = merge(left, right)
    total = left_count + right_count+s_count
    return merged, total


nums = [1, 3, 2, 3, 1]
result, count = merge_sort(nums)
print(count)  