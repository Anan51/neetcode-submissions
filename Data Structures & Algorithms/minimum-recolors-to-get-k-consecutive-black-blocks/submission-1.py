class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = 0
        BCount = 0
        WCount = 0
        minCount = len(blocks)

        for r in range(len(blocks)):
            if blocks[r] == "B":
                BCount += 1
            elif blocks[r] == "W":
                WCount += 1
            while WCount + BCount > k:
                if (blocks[l] == "B"):
                    BCount -= 1
                    l += 1
                elif (blocks[l] == "W"):
                    WCount -= 1
                    l += 1
            print(l, r, blocks[l:r], BCount, WCount)
            if (WCount + BCount == k):
                minCount = min(minCount, WCount)
            
        return minCount