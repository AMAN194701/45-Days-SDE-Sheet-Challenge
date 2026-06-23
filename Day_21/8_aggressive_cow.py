# Aggressive Cows : Detailed Solution
# Problem Statement: You are given an array 'arr' of size 'n' which denotes the position of stalls. You are also given an integer 'k' which denotes the number of aggressive cows.
# You are given the task of assigning stalls to 'k' cows such that the minimum distance between any two of them is the maximum possible. Find the maximum possible minimum distance.

# Example 1:
# Input Format: N = 6, k = 4, arr[] = {0,3,4,7,10,9}

# Result: 3
# Explanation:
# The maximum possible minimum distance between any two cows will be 3 when 4 cows are placed at positions {0, 3, 7, 10}. 
# Here the distances between cows are 3, 4, and 3 respectively.
# We cannot make the minimum distance greater than 3 in any ways.


# --------------------------------------------------
# Brute Force Approach
# TC : O((max(arr)-min(arr)) * n)
# SC : O(1)
# --------------------------------------------------

def can_place(arr, cows, dist):

    count_cows = 1      # Place 1st cow at first stall
    last = arr[0]

    for i in range(1, len(arr)):
        # Place next cow if distance condition is satisfied
        if arr[i] - last >= dist:
            count_cows += 1
            last = arr[i]
        if count_cows >= cows:
            return True
    return False
def aggressive_cows(arr, cows):
    # Sort the stalls
    arr.sort()
    # Maximum possible distance
    max_dist = arr[-1] - arr[0]

    # try every possible distance
    for dist in range(1, max_dist + 1):

        # if this distance is not possible,
        # previous distance was the answer
        if not can_place(arr, cows, dist):
            return dist - 1

    return max_dist

arr = [0, 3, 4, 7, 9, 10]
k = 4

print(aggressive_cows(arr, k))
