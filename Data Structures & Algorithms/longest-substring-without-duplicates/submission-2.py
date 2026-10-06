class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        i, j, maxLen = 0, 1, 0
        if len(s) < 2:
            return len(s)
        seen[s[i]] = 1

        while j < len(s):
            if s[j] not in seen or seen[s[j]] == 0:
                seen[s[j]] = 1
                j += 1
                maxLen = max(maxLen, j-i)
            else:
                seen[s[i]] -= 1
                i += 1
        print(seen)
        return maxLen

                
            

            