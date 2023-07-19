class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Check if three values are increasing as we go through list.
        val1 = float('inf')
        val2 = float('inf')
        for i in nums:
            # Select lowest value as we scan through nums.
            if (i < val1):
                val1 = i
            # If still possible and subsequent value is larger, select it as val2.
            # Equal sign included to account for repeated values.
            elif (i < val2):
                val2 = i
            # Catch the third value if present.
            else:
                return True
        # If unable to catch such a sequence, return false.
        return False
