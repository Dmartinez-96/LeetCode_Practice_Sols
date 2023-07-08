class Solution {
    public boolean increasingTriplet(int[] nums) {
        double val1 = 1.0 / 0.0;
        double val2 = 1.0 / 0.0;
        for (int i = 0; i < nums.length; i++) {
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
}