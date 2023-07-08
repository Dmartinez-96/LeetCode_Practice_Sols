class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> answer(size(nums), 1);
        int prodval = 1;
        // Create left products
        for (int i = 1; i < size(nums); i++) {
            answer[i] = answer[i-1] * nums[i-1];
        }
        // Create right products and merge
        for (int i = size(nums) - 1; i >= 0; i--) {
            answer[i] *= prodval;
            prodval *= nums[i];
        }
        return answer;
    }
};