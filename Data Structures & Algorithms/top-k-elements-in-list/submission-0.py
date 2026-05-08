import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = sorted(nums)
        count = [[1, nums[0]]]
        ind = 0
        ret = []
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                count[ind][0] += 1
                count[ind][1] = nums[i]
            else:
                ind += 1
                count.append([1,nums[i]])
        count.sort(key=lambda x: x[0])
        print(count)
        for i in range(k):
            ret.append(count[len(count)-i-1][1])
        
        return ret
