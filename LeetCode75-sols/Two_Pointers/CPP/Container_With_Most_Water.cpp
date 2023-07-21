class Solution {
public:
    int maxArea(vector<int>& height) {
        int left_ptr = 0;
        int right_ptr = height.size() - 1;
        int max_area = 0;
        while (left_ptr < right_ptr) {
            if ((right_ptr - left_ptr) * (min(height[left_ptr], height[right_ptr])) > max_area) {
                max_area = (right_ptr - left_ptr) * (min(height[left_ptr], height[right_ptr]));
            }
            if (height[left_ptr] < height[right_ptr]) {
                left_ptr++;
            }
            else {
                right_ptr--;
            }
        }
        return max_area;
    }
};