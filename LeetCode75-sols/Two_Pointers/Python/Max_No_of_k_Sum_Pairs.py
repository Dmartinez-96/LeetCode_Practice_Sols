class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left_ptr = 0
        right_ptr = len(nums) - 1
        if (len(nums) == 0):
            return 0
        while left_ptr < right_ptr:
            if (nums[left_ptr] + nums[right_ptr] == k):
                left_ptr += 1
                right_ptr -= 1
                count += 1
            elif (nums[left_ptr] + nums[right_ptr] < k):
                left_ptr += 1
            else:
                right_ptr -= 1
        return count