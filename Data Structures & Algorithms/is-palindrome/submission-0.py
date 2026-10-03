class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(filter(str.isalnum, s))
        s = s.lower()
        print(s)
        for i in range(len(s)//2):
            print(i)
            if s[i] != s[len(s)-i-1]:
                return False
        return True