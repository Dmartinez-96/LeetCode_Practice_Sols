class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        int orig_max = *max_element(candies.begin(), candies.end());
        int i = 0;
        vector<bool> result = {};
        while (i < candies.size()) {
            if (candies[i] + extraCandies >= orig_max) {
                vector<bool> a = { true };
                result.insert(result.end(), a.begin(), a.end());
            }
            else {
                vector<bool> a = { false };
                result.insert(result.end(), a.begin(), a.end());
            }
            i++;
        }

        return result;
    }
};