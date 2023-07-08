class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            answer[i] = 1;
        }
        int prodval = 1;
        // Create left products
        for (int i = 1; i < nums.length; i++) {
            answer[i] = answer[i-1] * nums[i-1];
        }
        // Create right products and merge
        for (int i = nums.length - 1; i >= 0; i--) {
            answer[i] *= prodval;
            prodval *= nums[i];
        }
        return answer;
    }
}