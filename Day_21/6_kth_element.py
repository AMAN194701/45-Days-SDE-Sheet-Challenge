# K-th Element of two sorted arrays
# Problem Statement: Given two sorted arrays a and b of size m and n respectively. Find the kth element of the final sorted array.

# Example 1:
# Input: a = [2, 3, 6, 7, 9], b = [1, 4, 8, 10], k = 5  
# Output: 6  
# Explanation:
#  The final sorted array would be [1, 2, 3, 4, 6, 7, 8, 9, 10]. The 5th element of this array is 6.

# --------------------------------------------------
# Brute Force Approach 
# TC : O((m+n) log (m+n))
# SC : O(m+n)
# --------------------------------------------------
def Solution(a,b,k):
    merged = a+b 
    merged.sort()
    return merged[k-1]


a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(Solution(a, b, k))

# --------------------------------------------------
# Optimal Approach (Binary Search)
# TC : O(log(min(m,n)))
# SC : O(1)
# --------------------------------------------------
def opt_kth_element(a,b,k):
    n1= len(a)
    n2 = len(b)

    # search in the smaller array
    if n1>n2:
        return opt_kth_element(b, a, k)
    
    low = max(0, k-n2)
    high = min(k,n1)

    while low<=high :

        mid1= (low+high)//2 
        mid2 = k - mid1

        # Find l1, l2, r1, r2
        l1 = float('-inf') if mid1==0 else a[mid1-1]
        l2 = float('-inf') if mid2==0 else b[mid2-1]
        r1 = float('inf') if mid1==n1 else a[mid1]
        r2 = float('inf') if mid2==n2 else b[mid2]  

        # check for correct partition
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2:
            high = mid1 -1
        else:
            low = mid1 +1   
    return -1

a = [2, 3, 6, 7, 9]
b = [1, 4, 8, 10]
k = 5
print(opt_kth_element(a, b, k))