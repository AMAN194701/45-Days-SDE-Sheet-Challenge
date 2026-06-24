import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # count frequency
        for num in nums:
            freq[num] = freq.get(num,0)+1
        heap = []

        # keep only k elements
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))
            if len(heap) > k:
                heapq.heappop(heap)
        ans = []

        while heap:
            count,num = heapq.heappop(heap)
            ans.append(num)

        return ans