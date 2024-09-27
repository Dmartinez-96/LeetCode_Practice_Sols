class Solution:
    def trap(self, height: List[int]) -> int:
        # Check for no elevation map
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if height[left] < height[right]:
                # Move left pointer to the right
                left += 1
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])
            else:
                # Move right pointer to the left
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])
        return water
