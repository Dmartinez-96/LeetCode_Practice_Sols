class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int flow_len = 0;
        for (int j: flowerbed) {
            flow_len += 1;
        }
        int viable_count = 0;
        if (n==0) {
            return true;
        }
        for (int i = 0; i < flow_len; i++) {
            if (flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && (i == flow_len - 1 || flowerbed[i+1] == 0)) {
                flowerbed[i] = 1;
                viable_count += 1;
            }
        }
        if (viable_count >= n) {
            return true;
        }
        return false;
    }
};