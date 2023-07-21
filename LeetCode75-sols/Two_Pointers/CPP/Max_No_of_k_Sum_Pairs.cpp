class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int count = 0;
        int left_ptr = 0;
        int right_ptr = nums.size() - 1;
        if (nums.size() == 0) {
            return 0;
        }
        while (left_ptr < right_ptr) {
            if (nums[left_ptr] + nums[right_ptr] == k) {
                left_ptr++;
                right_ptr--;
                count++;
            }
            else if (nums[left_ptr] + nums[right_ptr] < k) {
                left_ptr++;
            }
            else {
                right_ptr--;
            }
        }
        return count;
    }
};