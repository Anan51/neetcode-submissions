class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(sorted(set(nums)))
        res = 0
        l = 0
        r = 0
        if len(nums) < 2:
            return len(nums)
        while l <= r and r+1 < len(nums):
            if nums[r+1] == nums[r] + 1:
                r += 1
            else:
                l = r+1
                r += 1
            res = max(r-l+1, res)
        return res
        