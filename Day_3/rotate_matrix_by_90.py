# Rotate the matrix by 90 degrees clockwise
# T.C => O(n^2) - since nested loop
# S.C => O(n^2) - new matrix get created which is of same size 

def Solution(matrix):
    # Size of the matrix
    n=len(matrix)

    # Rotated new matrix
    rotated= [[0]* n for _ in range(n)]

    # Traversing each element row by row
    for i in range(n): # row
        for j in range(n): # column

            # Moving current element to its rotated position
            rotated[j][n-i-1]=matrix[i][j] 

    return rotated

print(Solution([
    [1,2,4],
    [4,5,6],
    [7,8,9]
         ]))
# Conclusion :- Every element at position (i, j) moves to (j, n-1-i) after a 90° clockwise rotation.



# Optimal Approach :
# Here we will Transpose the matrix and then we will reverse the elements row by row to rotated it by 90 degree
# while transposing the diagonal elements remains at the same location 
# T.C => O(n^2)   - Nested loop
# S.C => O(1)     - No extra space is used 

def Solution(matrix):
    n=(len(matrix))

    # Transpose the matrix 
    for i in range(n):
        for j in range(i+1,n):  # j is strating from i+1 to avoid reswapping (visit only upper triangle)
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j] #  Swap

    # Reversing the each row 
    for i in range(n):
        matrix[i].reverse()

    return matrix

print(Solution([
    [1,2,4],
    [4,5,6],
    [7,8,9]
         ]))





