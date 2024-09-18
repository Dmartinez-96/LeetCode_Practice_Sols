/**
 * @param {string} word1
 * @param {string} word2
 * @return {string}
 */
var mergeAlternately = function(word1, word2) {
    let result = "";
    let i = 0;
    let len1 = word1.length;
    let len2 = word2.length;

    while ((i < len1) || (i < len2)) {
        if (i < len1) {
            result += word1[i];
        }
        if (i < len2) {
            result += word2[i];
        }
        i++;
    }
    return result;
};
