class Solution:
    def find(self, nums: List[int], guess: int) -> int:
        start = 0
        end = start + guess
        s = sum(nums[start:end])

        while (end < len(nums)):
            l = end - start
            if (l - s) <= 1:
                return s
            s -= nums[start]
            start += 1

            s += nums[end]
            end += 1
        
        l = end - start
        if ((l - s) <= 1):
            return s

        return -1
    
    def longestSubarray(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)
        ans = 0

        while (low <= high):
            middle = (low + high) // 2
            possible = self.find(nums, middle)
            if (possible != -1):
                ans = max(ans, middle - 1)
                low = middle + 1
            else:
                high = middle - 1
        return ans
