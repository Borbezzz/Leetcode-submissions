class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num,0) +1

        
        result = []

        for _ in range(k):
            highest = 0
            index = 0
            for key, val in count.items():
                if val > highest:
                    highest = val
                    index = key
            result.append(index)
            del count[index]
        

        return result