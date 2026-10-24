class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        l, i = 0, 1
        if (len(s) < 2):
            return len(s)
        seen = set()
        seen.add(s[0])
        while i < len(s):
            if s[i] not in seen:
                seen.add(s[i])
                i += 1
                maxLen = max(maxLen, i-l)
            else:
                seen.remove(s[l])
                l += 1
        return maxLen