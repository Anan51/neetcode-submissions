class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = 0
        count = 0
        for i in nums:
            if count == 0:
                c = i
                count = 1
            elif i == c:
                count += 1
            else:
                count -= 1
            
        return c
        