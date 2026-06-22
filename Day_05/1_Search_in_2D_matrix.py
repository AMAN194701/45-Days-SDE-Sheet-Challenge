# Search in 2D matrix brute force approach 


# --------------------------------------------------
# Approach 
# TC : O( row * col ) - nested Loop
# SC : O(1)   - since no extra space is used  
# --------------------------------------------------
print("-"*30)
def Solution(arr,target):
    row=len(arr)
    col=len(arr[0])
    for i in range(row):
        for j in range(col):
            if arr[i][j]==target:
                return True 
    return False 
arr=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
result =Solution(arr,3) 
print(result)



# --------------------------------------------------
# Using binary Search Approach (Optimal approach)
# TC : O(log (row * colm))
# SC : O(1)
# --------------------------------------------------
def Solution(matrix , target):
    # Calculating no of rows and colm(size of matrix)
    rows= len(matrix)
    cols= len(matrix[0])

    # Boundaries of search
    low= 0 
    high = rows*cols-1 

    # Continue until it became empty
    while low<=high:
        mid= (low+high)//2 

        # Finding position in matrix
        row= mid//cols 
        col = mid % cols 

        # Compare current element with target and update search boundary
        if matrix[row][col]==target:
            return True 
        elif matrix[row][col]< target:
            low=mid+1
        else:
            high= mid-1
    return False

matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]
]

target = 16
result= Solution(matrix, target)
print(result)

print("-"*30)