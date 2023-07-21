class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        max_area = 0
        while (left_ptr < right_ptr):
            curr_wdw_area = (right_ptr - left_ptr) * (min(height[left_ptr],height[right_ptr]))
            if (curr_wdw_area > max_area):
                max_area = curr_wdw_area
            if (height[left_ptr] < height[right_ptr]):
                left_ptr += 1
            else:
                right_ptr -= 1
        return max_area
