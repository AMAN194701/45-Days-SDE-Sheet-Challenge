# --------------------------------------------------
# Brute force approach 
# TC : O(n^2) - nested loop 
# SC : O(n^2) - Storing complete triangle
# --------------------------------------------------
def brute_pascal_triangle(num):
    triangle=[]

    # For each row number of elements filled with 1
    for i in range(num):
        row= [1]*(i+1)

        # updating the middle element vales using previous row
        for j in range(1,i):
            row[j]=triangle[i-1][j-1] + triangle[i-1][j]
        # appending the final row values
        triangle.append(row)
    return triangle 

result= brute_pascal_triangle(5)
print(result)
print("-"*50)

# --------------------------------------------------
# Optimal Approach 
# TC : O(n^2) - generating n rows, each row takes O(row) time
# SC : O(n^2) - complete triangle get stored
# --------------------------------------------------

# function to generate the single row using nCr
def generate_row(num):
    # first element of each row 
    row= [1]
    # current nCr value 
    ans =1

    # Generate othr elements of row
    for r in range(num):
        # find next nCr using previous nCr
        ans= ans*(num-r)
        ans= ans//(r+1)

        row.append(ans)
    return row 

# Function to generate the complete triangle
def gen_pascal_triangle(num):
    triangle=[]
    for row in range(num):
        triangle.append(generate_row(row))
    return triangle


result= gen_pascal_triangle(5)
print(result)
