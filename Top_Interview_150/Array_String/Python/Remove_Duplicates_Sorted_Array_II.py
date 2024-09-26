class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dict = {}
        curr_idx = 0
        n_orig = len(nums)
        num_deleted = 0
        while (curr_idx < n_orig):
            if nums[curr_idx - num_deleted] in num_dict.keys():
                num_dict[nums[curr_idx - num_deleted]] += 1
                if (num_dict[nums[curr_idx - num_deleted]] > 2):
                    nums.pop(curr_idx - num_deleted)
                    num_deleted += 1
            else:
                num_dict[nums[curr_idx - num_deleted]] = 1
            curr_idx += 1
        return len(nums)
