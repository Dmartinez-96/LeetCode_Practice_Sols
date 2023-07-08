class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        float val1 = numeric_limits<float>::infinity();
        float val2 = numeric_limits<float>::infinity();
        for (int i = 0; i < size(nums); i++) {
            if (nums[i] <= val1) {
                val1 = nums[i];
            }
            else if (nums[i] <= val2) {
                val2 = nums[i];
            }
            else {
                return true;
            }
        }
        return false;
    }
};