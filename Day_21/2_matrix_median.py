# Problem Statement:
# Given a row-wise sorted matrix of size M*N, where M is no. of rows and N is no. of columns, find the median in the given matrix.
# Note: M*N is odd.

# Input: M = 3, N = 3, matrix[][] =
# 1 4 9 
# 2 5 6
# 3 8 7
# Output: 5
# Explanation: 
# If we find the linear sorted array, the array becomes 1 2 3 4 5 6 7 8 9. Therefore, median = 5

# --------------------------------------------------
# Brute force approach 
# TC : O(m*n log (m*n))
# SC : O(m * n)
# --------------------------------------------------
def solution(matrix):
    arr=[]
    for row in matrix :
        for element in row :
            arr.append(element)
    arr.sort()
    return arr[len(arr)//2]

matrix = [
    [1, 4, 9],
    [2, 5, 6],
    [3, 8, 7]
]
print(solution(matrix))

# --------------------------------------------------
# Optimal approach 
# TC : O(rows × log(max - min) × log(cols))
# SC : O(1)
# --------------------------------------------------
import bisect
def opt_solution(matrix):
    m = len(matrix)
    n = len(matrix[0])
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)
    
    req = (m*n +1 )//2
    while low <= high :
        mid = (low + high)//2
        count = 0 
        for row in matrix :
            count += bisect.bisect_right(row,mid)
        if count < req :
            low = mid +1
        else :
            high = mid -1  
    return low 

matrix = [
    [1,3,5],
    [2,6,9],
    [3,6,9]
]
print(opt_solution(matrix))