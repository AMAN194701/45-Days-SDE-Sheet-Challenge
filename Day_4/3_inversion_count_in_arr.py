# Inversion is when a bigger number comes before the smaller number
# --------------------------------------------------
# Brute force approach: Here we are both count and pair 
# TC : O(n^2) - nested loop
# SC : O(n^2) - since we are storing every inversion pair
# --------------------------------------------------
def inversion_count(arr):
    pair=[]
    n = len(arr)
    count= 0 
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                pair.append((arr[i], arr[j] ))
                count+=1 

    return count , pair
arr= [5,3,2,1,4]
count,pair= inversion_count(arr)
print("total count", count)
print("pair are : ", pair)
print("-"*50)

# --------------------------------------------------
# Optimal Approach 
# TC : O(n log n) - since using merge sort concept
# SC : O(n)       - for storing result
# --------------------------------------------------
def merge_sort(arr):
    n= len(arr)

    # base case
    if n <=1:
        return arr ,0
    
    mid = n//2
    # Recursively sort and count the inversion 
    left, left_inv= merge_sort(arr[:mid])
    right, right_inv= merge_sort(arr[mid:])

    merged, split_inv = merge(left, right)

    total = left_inv + right_inv +split_inv 
    return merged, total 

# function to merge two sorted arr
def merge(left,right):
    result= []
    # pointer for left and right arr
    i =0 
    j =0
    inversion_count=0 

    # comparing elements from both side and appeding 
    while i < len(left) and j <len(right):
        if left[i]<= right[j]:
            result.append(left[i])
            i+=1 
        else:
            result.append(right[j])

            inversion_count+= len(left)- i 
            j+=1 

    result.extend(left[i:])
    result.extend(right[j:])

    return result, inversion_count

sorted_arr, count = merge_sort(arr)
print("Original :", arr)
print("Sorted Array:", sorted_arr)
print("Total Count:", count)