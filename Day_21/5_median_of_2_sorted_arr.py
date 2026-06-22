# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# --------------------------------------------------
# Brute Force Approach
# TC - O(m+n log m+n)
# SC - O(n)
# --------------------------------------------------

def Solution(nums1, num2):
    merged = nums1 +num2
    merged.sort()
    n = len(merged)
    if n %2==1:
        return (merged[n//2])
    else :
        return (merged[n//2]+ merged[n//2 -1])/2

nums1 = [1,3]
nums2 = [2,4]
print(Solution(nums1, nums2))

# --------------------------------------------------
# Optimal Approach (Binary Search)
# TC - 
# Sc - 
# -------------------------------------------------- 
def find_median_sorted_arrays(nums1, nums2):
    n1= len(nums1)
    n2 = len(nums2)

    # search in the smaller array
    if n1>n2:
        return find_median_sorted_arrays(nums2, nums1)
    low=0 
    high = n1 

    # Total num of element needed in left side of partition
    left = (n1+n2+1)//2

    while low<=high:
        mid1 = (low+high)//2

        mid2 = left - mid1

        # find l1 , r1, l2,r2
        l1 = float('-inf') if mid1==0 else nums1[mid1-1]
        l2 = float('-inf') if mid2==0 else nums2[mid2-1]
        r1 = float('inf') if mid1==n1 else nums1[mid1]
        r2 = float('inf') if mid2==n2 else nums2[mid2]  

        # check for correct partition
        if l1<=r2 and l2<=r1:
            # check for odd or even
            if (n1+n2)%2==0:
                return (max(l1,l2)+min(r1,r2))/2
            else:
                return max(l1,l2)
            
        elif l1>r2:
            high = mid1-1
        else:
            low = mid1+1
    return 0 

nums1 = [1,2]
nums2 = [3,4]

print(find_median_sorted_arrays(nums1, nums2))


