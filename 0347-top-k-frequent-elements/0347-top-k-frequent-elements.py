class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = {}
        freq_arr = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for n, c in count.items():
            freq_arr[c].append(n)

        result = []
        for i in range(len(freq_arr) - 1, 0, -1):
            for n in freq_arr[i]:
                result.append(n)
                if len(result) == k:
                    return result