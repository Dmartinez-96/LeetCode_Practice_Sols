class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        counterDict = {}
        currIdx = 0
        while (currIdx < n):
            if nums[currIdx] in counterDict.keys():
                counterDict[nums[currIdx]] += 1
            else:
                counterDict[nums[currIdx]] = 1
            currIdx += 1
        return max(counterDict, key=counterDict.get)
