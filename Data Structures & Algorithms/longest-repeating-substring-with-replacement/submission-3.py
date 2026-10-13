class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        res = 0
        seen = set(s)
        
        for c in seen:
            l = 0
            count = 0
            for r in range(n):
                if (s[r] == c):
                    count += 1
                while r - l - count + 1 > k:
                    if (s[l] == c):
                        count -= 1
                    l += 1
                res = max(res, r - l + 1)
        return res
