import heapq
class Solution:
    def mergeArrays(self, mat):
        heap = []
        ans = []
        # put 1st element of every row
        for row in range(len(mat)):
            heapq.heappush(heap, (mat[row][0], row, 0))
        while heap:
            val, row, col = heapq.heappop(heap)
            ans.append(val)

            # push next element from same row
            if col + 1 < len(mat[row]):
                heapq.heappush(heap, (mat[row][col + 1], row, col + 1))

        return ans