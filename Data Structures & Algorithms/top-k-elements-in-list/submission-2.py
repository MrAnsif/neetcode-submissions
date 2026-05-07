import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for i in nums:
            numMap[i] = 1+numMap.get(i, 0)
        heap = []
        for num, freq in numMap.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for freq, num in heap]   