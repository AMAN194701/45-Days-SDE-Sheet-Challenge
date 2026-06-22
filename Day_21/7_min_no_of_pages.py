# Allocate Minimum Number of Pages
# Problem Statement: Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
# Allocate books in such a way that:

# Each student gets at least one book.
# Each book should be allocated to only one student.
# Book allocation should be in a contiguous manner.
# You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1

# Examples
# Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
# Result: 113
# Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

# --------------------------------------------------
# Brute force approach 
# TC : O(n^2)
# SC : O(1)
# --------------------------------------------------

def min_pages(arr,m):
    ans= float('inf')
    for i in range(1,len(arr)):
        std1 = sum(arr[:i])
        std2 = sum(arr[i:])

        max_pages= max(std1, std2)
        ans = min(ans, max_pages)
    return ans 

arr = [12, 34, 67, 90]
m = 2
print(min_pages(arr, m))

# --------------------------------------------------
# Optimal approach 
# TC : O(n * log(sum - max))
# SC : O(1)
# --------------------------------------------------

class Solution:
    def countStudents(self, arr, pages):
        students = 1
        pages_student = 0
        for num in arr:
            if pages_student + num <= pages:
                pages_student += num
            else:
                students += 1
                pages_student = num
        return students
    
    def findPages(self, arr, k):
        n = len(arr)

        # impossible case
        if k > n:
            return -1

        low = max(arr)
        high = sum(arr)

        while low <= high:
            mid = (low + high) // 2
            students = self.countStudents(arr, mid)
            if students > k:
                low = mid + 1
            else:
                high = mid - 1

        return low

