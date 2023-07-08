class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Remove trivial cases
        if len(nums) < 3:
            return False
        # Check if three values are increasing as we go through list
        val1 = float('inf')
        val2 = float('inf')
        for i in nums:
            if (i <= val1):
                val1 = i
            elif (i <= val2):
                val2 = i
            else:
                return True
        return False