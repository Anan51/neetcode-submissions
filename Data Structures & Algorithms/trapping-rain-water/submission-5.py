class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefMax = [0]*n
        suffMax = [0]*n
        prefMax[0] = height[0]
        suffMax[-1] = height[-1]
        res = 0
        for i in range(1,n):
            prefMax[i] = max(prefMax[i-1], height[i])
        for i in range(n-2, -1, -1):
            suffMax[i] = max(suffMax[i+1], height[i])
        
        for i in range(n):
            res += min(prefMax[i], suffMax[i]) - height[i]
        return res