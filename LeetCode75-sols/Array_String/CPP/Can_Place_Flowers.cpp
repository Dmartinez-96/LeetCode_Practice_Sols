class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int flow_len = flowerbed.size();
        int viable_count = 0;
        if (n == 0) {
            return true;
        }
        for (int i = 0; i < flow_len; i++) {
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == flow_len - 1 or flowerbed[i+1] == 0)) {
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