class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        c = nums[(r+l)//2]
        while c != target and r-l > 1:
            c = nums[(r+l)//2]
            if c == target:
                return (r+l)//2
            if c > target:
                r = (l+r)//2
            else:
                l = (l+r)//2
        if c == target:
            return (l+r)//2
        elif nums[l] == target:
            return l
        elif nums[r] == target:
            return r
        else:
            return -1
        