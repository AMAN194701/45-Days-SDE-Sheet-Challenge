# Maximum Sum Combination

# Problem Statement: Given two integer arrays nums1 and nums2 and an integer k,
# return the maximum k valid sum combinations from all possible sum combinations using the elements of nums1 and nums2. 
# A valid sum combination is made by adding one element from nums1 and one element from nums2. Return the answer in non-increasing order.
# EG. Input : nums1 = [7, 3], nums2 = [1, 6], k = 2
# Output : [13, 9]
# Explanation : The 2 maximum combinations are made by: nums1[0] + nums2[1] = 13 nums1[1] + nums2[1] = 9 

# --------------------------------------------------
# Brute Force approach :
# TC : O(n^2 log n)
# SC : O(n^2)
# --------------------------------------------------
class Solution():
    def max_combn(self,x,y,k):
        sums=[]
        # generate all possible sum
        for i in range(len(x)):
            for j in range(len(y)):
                sums.append(x[i]+y[j])
        # sort the sum in descending order 
        sums.sort(reverse=True)
        # return the 1st kth element 
        return sums[:k]
    
x = [1,4,2,3]
y = [2,5,1,6]
k = 4

Q1 = Solution()
print("Brute Force : ",Q1.max_combn(x, y, k))


# --------------------------------------------------
# Optimal approach :
# TC : O(n log n + k log k)
# SC : O(k)
# --------------------------------------------------
import heapq
class Solution:
    def max_sum_combn(self, A, B, k):
        n = len(A)
        A.sort(reverse=True)
        B.sort(reverse=True)
        heap = []
        visited = set()
        # push largest sum
        heapq.heappush(heap, (-(A[0]+B[0]),0,0))
        visited.add((0,0))
        ans = []

        while k > 0:
            curr_sum,i,j = heapq.heappop(heap)
            ans.append(-curr_sum)

            if i+1 < n and (i+1,j) not in visited:
                heapq.heappush(heap, (-(A[i+1]+B[j]),i+1,j))
                visited.add((i+1,j))

            if j+1 < n and (i,j+1) not in visited:
                heapq.heappush(heap, (-(A[i]+B[j+1]),i,j+1))
                visited.add((i,j+1))

            k -= 1

        return ans
    
A = [1, 4, 2, 3]
B = [2, 5, 1, 6]
k = 4

Q2 = Solution()
print("Optimal :", Q2.max_sum_combn(A, B, k))