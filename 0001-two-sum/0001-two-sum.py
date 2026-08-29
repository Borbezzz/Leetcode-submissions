class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, num in enumerate(nums):
            find = target - num
            
            if find in hash:
                return i, hash[find]
            else:
                hash[num] = i