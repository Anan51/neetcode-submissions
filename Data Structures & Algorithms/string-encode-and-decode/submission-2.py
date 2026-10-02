class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] += "\\endstring"
        print("|STRINGSPLIT|".join(strs))
        return "|STRINGSPLIT|".join(strs)

    def decode(self, s: str) -> List[str]:
        print(s.split("|STRINGSPLIT|"))
        print("".join(s.split("|STRINGSPLIT|")))
        print("".join(s.split("|STRINGSPLIT|")).split("\\endstring"))
        return "".join(s.split("|STRINGSPLIT|")).split("\\endstring")[:-1]
        
