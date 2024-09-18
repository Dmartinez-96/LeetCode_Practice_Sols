/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
bool* kidsWithCandies(int* candies, int candiesSize, int extraCandies, int* returnSize) {
    // Find max number of candies a kid has
    int orig_max = candies[0];
    for (int i = 1; i < candiesSize; i++) {
        if (candies[i] > orig_max) {
            orig_max = candies[i];
        }
    }
    
    // Allocate memory for result
    bool* result = (bool*)malloc(candiesSize * sizeof(bool));
    if (result == NULL) {
        *returnSize = 0;
        return NULL;
    }

    // Can each kid have greatest number of candies?
    for (int i = 0; i < candiesSize; i++) {
        if (candies[i] + extraCandies >= orig_max) {
            result[i] = true;
        } else {
            result[i] = false;
        }
    }

    *returnSize = candiesSize;

    return result;
}
