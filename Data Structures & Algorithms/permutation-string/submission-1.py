class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        n2 = len(s1)
        s1 = sorted(s1)
        l = 0
        while l + n2 <= n:
            print(s2[l:l+n2])
            if sorted(s2[l:l+n2]) == s1:
                return True
            else:
                l += 1
        return False
        