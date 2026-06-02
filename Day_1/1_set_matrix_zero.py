# Better approach : Creating a marker matrix of all 0s, contaning same number of rows and colms 
# T.C => O(row * col)
# S.C => O(row + col)

def Solution(matrix):
    row= len(matrix)   # No of rows
    col=len(matrix[0]) # No of cols 

    # creating marker arr of rows and cols contaning all 0 
    row_marker= row*[0] 
    col_marker= col*[0]

    # If 0 is found in the original matrix 
    for i in range(row):
        for j in range(col):
            if matrix[i][j]==0:
                # Then converting marker row and colm as 1 
                row_marker[i]=1
                col_marker[j]=1 
    
    # Now checking all the marker place where 1 is present and and in the same location of orignal matrix converting it into 0 
    for i in range(row):
        for j in range(col):
            if row_marker[i]==1 or col_marker[j]==1:
                matrix[i][j]=0

    
