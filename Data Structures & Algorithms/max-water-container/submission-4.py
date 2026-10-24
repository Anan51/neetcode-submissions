class Solution:
    def maxArea(self, heights: List[int]) -> int:
        tempMax = 0
        l, r, = 0, len(heights)-1

        while l < r:
            tempMax = max(tempMax, (r - l)*min(heights[r], heights[l]))
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1
        return tempMax