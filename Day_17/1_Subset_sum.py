class Solution:
    def set_values(self, arr):
        result=[]
        def actual_work(index, curr_sum):
            
            # Base case if it is on the last index
            if index == len(arr):
                result.append(curr_sum)
                return 

            # take the number and add it 
            actual_work(index+1, curr_sum + arr[index])

            # Do not take the number  
            actual_work(index +1, curr_sum)

        actual_work(0,0)

        result.sort()
        return result 
    

s1 = Solution()
arr=[5, 2, 1]
print(s1.set_values(arr))