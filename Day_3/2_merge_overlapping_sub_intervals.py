# Merge Overlapping Sub-intervals
# -------------------------------------------------------
# Brute Force Approach
# T.C => O(n^2)
# S.C => O(n)
# -------------------------------------------------------


def Solution(intervals):
    intervals.sort()
    i = 0 
    n=len(intervals) # Length of list
    result=[] # Store the updated values

    # Loop though each interval
    while i<n:
        # Start and end of current interval
        start= intervals[i][0]
        end=intervals[i][1]

        # j variable to check next interval
        j=i+1

        # update the end variable if overlap is present
        while j<n and intervals[j][0]<=end:
            end=max(end,intervals[j][1])
            j+=1 # to check the next interval

        result.append([start,end])

        # move to next non-overlapping interval
        i=j 
    return result 

# -------------------------------------------------------
# Optimal approach 
# T.C : O(n log n)
# S.C : O(n)
# -------------------------------------------------------


def solution(intervals):

    intervals.sort() 

    # list to store the final result 
    merged=[]

    # Moving through each intervals
    for interval in intervals:
        # If merged is empty OR there is no overlap
        # (previous interval ends before current interval starts)
        if not merged or merged[-1][1]< interval[0]:
            # Add current interval as a new interval
            merged.append(interval)

        else: # i.e current interval start before previous one ends so overlap exisit
            # Update the last element of merged
            merged[-1][1]=max(merged[-1][1],interval[1])
    return merged 

# ============================================================
# Test Cases
# ============================================================

test_cases = [
    [[1,3],[2,6],[8,10],[15,18]],    
    [[1,4],[4,5]],                   
    [[1,2],[4,5],[7,8]],             
    [[1,10],[2,3],[4,5],[6,7]],      
]

for intervals in test_cases:

    print(f"Input           : {intervals}")
    print(f"Output_Brute    : {solution(intervals)}")
    print(f"Output_Opt      : {Solution(intervals)}")
    print("-" * 40)
