class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = ["".join(sorted(i)) for i in strs]
        count = 0
        seen = {}
        for i in range(len(sortedStrs)):
            if sortedStrs[i] in seen:
                seen[sortedStrs[i]].append(i)
            else:
                seen[sortedStrs[i]] = [i]
        return [[strs[j] for j in seen[i]] for i in seen]
        