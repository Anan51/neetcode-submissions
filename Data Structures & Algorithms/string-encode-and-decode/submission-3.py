class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] += "\\endstring"
        return "|STRINGSPLIT|".join(strs)

    def decode(self, s: str) -> List[str]:
        return "".join(s.split("|STRINGSPLIT|")).split("\\endstring")[:-1]
        
