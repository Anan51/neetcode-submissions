class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        print(nums)
        res = []

        l = 0
        r = n-1
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i-1]:
                continue

            l,r = i+1, n-1
            while l < r:
                c = a + nums[l] + nums[r]
                if c > 0:
                    r -= 1
                elif c < 0:
                    l += 1
                else:
                    res.append([nums[l], a, nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
                