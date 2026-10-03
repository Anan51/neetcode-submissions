class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n-1
        while l < r:
            c = numbers[l] + numbers[r]
            if c == target:
                return [l+1, r+1]
            elif c < target:
                l += 1
            elif c > target:
                r -= 1