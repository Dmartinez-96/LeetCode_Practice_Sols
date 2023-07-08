class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prodval = 1
        # Create left products
        for i in range(1,len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        # Create right products and merge
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= prodval
            prodval *= nums[i]
        return answer