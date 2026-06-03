# --------------------------------------------------------------------------------
# Optimal Way :
# TC => O(m+n)
# SC => O(1)
# --------------------------------------------------------------------------------

def Opt_Solution(num1, num2, m , n):
    i = m-1 # last valid index at at num1
    j = n-1 # last index of num2
    k=m+n-1 # last index of num1

    # Merging from back  
    while i>=0 and j >= 0 :
        if num1[i]>num2[j]:
            num1[k]= num1[i]
            i-=1
        else:
            num1[k]=num2[j]
            j-=1
        k-=1

    # if any element is still present in num2 then copy them in num1
    while j>=0:
        num1[k]=num2[j]
        k-=1
        j-=1
    return num1

# --------------------------------------------------------------------------------
# Test Case 
# --------------------------------------------------------------------------------
test_cases = [
    ([1,3,5,0,0,0], [2,4,6], 3, 3),      
    ([1,2,3,0,0,0], [4,5,6], 3, 3),     
    ([4,5,6,0,0,0], [1,2,3], 3, 3),     
    ([1,0], [2], 1, 1),               
    ([2,0], [1], 1, 1),                  
    ([1], [], 1, 0),                   
    ([0], [1], 0, 1),   
    ([1, 3, 5, 0, 0, 0], [2, 4, 6],3,3)               
]
for nums1, nums2, m, n in test_cases:

    print(f"nums1 : {nums1}")
    print(f"nums2 : {nums2}")

    print("optimal_output :", Opt_Solution(nums1, nums2, m, n))


    print("-" * 40)

