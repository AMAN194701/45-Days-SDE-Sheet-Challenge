# --------------------------------------------------
# Merge Sort 
# TC - O(n log n)
# SC - O(n)
# --------------------------------------------------
def merge_sort(arr):
    n = len(arr)

    # Base case 
    if n <= 1:
        return arr
    
    # Divinding the arr
    mid=n//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left,right)

# Function to merge two arr
def merge(left, right):
    result = []
    # pointer for left and right arr
    i = 0
    j = 0
    
    # compare both arr
    while i < len(left) and j < len(right):
        # condition for appending the small number from the arr
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    # Adding the remaning elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result 

arr =[4,3,5,8,6,3]
result= merge_sort(arr)
print(result)
        