class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        valmatches = [0] * n
        curr_idx = 0
        while (curr_idx < n):
            if nums[curr_idx] == val:
                valmatches[curr_idx] = 1
            curr_idx += 1
        curr_idx = 0
        deleted_pts = 0
        while (curr_idx < n):
            if (valmatches[curr_idx] == 1):
                nums.pop(curr_idx - deleted_pts)
                deleted_pts += 1
            curr_idx += 1
        n_not_val = len(nums)
        return n_not_val
