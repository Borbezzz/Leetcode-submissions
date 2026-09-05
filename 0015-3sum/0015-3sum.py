class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        n = len(nums)

        for a in range(n -  2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            l, r  = a + 1, n - 1
            while l < r:
                total = nums[a] + nums[l] + nums[r]
                if total == 0:
                    res.append([nums[a], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif total < 0:
                    l += 1
                else: 
                    r -= 1

        return res