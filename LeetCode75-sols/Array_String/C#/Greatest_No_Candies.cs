using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<bool> KidsWithCandies(int[] candies, int extraCandies) {
        // Find max no of candies a kid has
        int maxCandies = candies.Max();

        List<bool> result = new List<bool>();

        foreach (int candy in candies) {
            if (candy + extraCandies >= maxCandies) {
                result.Add(true);
            } else {
                result.Add(false);
            }
        }
        return result;
    }
}
