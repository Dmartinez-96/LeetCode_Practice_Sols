class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        orig_max = max(candies)
        return [True if (i + extraCandies) >= orig_max else False for i in candies]