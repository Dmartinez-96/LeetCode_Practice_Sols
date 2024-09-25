class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sumHeight = 0
        maxHeight = 0
        for i in range(len(gain)):
            sumHeight += gain[i]
            if (sumHeight >= maxHeight):
                maxHeight = sumHeight
        return maxHeight
