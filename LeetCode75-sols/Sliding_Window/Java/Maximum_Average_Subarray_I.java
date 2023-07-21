class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int curr = 0;
        double res = 0;
        for (int i = 0; i < k; i++) {
            curr += nums[i];
            res += nums[i];
        }
        for (int i = k; i < nums.length; i ++) {
            curr += nums[i] - nums[i-k];
            if (curr > res) {
                res = curr;
            }
        }
        return (res / k);
    }
}