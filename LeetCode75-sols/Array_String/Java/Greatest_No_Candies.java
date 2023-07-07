class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int orig_max = 0;
        for (int j: candies) {
            if (orig_max < j) {
                orig_max = j;
            }
        }
        List<Boolean> result = new ArrayList<>();
        for (int i: candies) {
            if (i + extraCandies >= orig_max) {
                result.add(true);
            }
            else {
                result.add(false);
            }
        }
        return result;
    }
}