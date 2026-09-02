class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        max_heap = []
        for num, freq in count.items():
            heapq.heappush(max_heap, (-freq, num))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(max_heap)[1])

        return result