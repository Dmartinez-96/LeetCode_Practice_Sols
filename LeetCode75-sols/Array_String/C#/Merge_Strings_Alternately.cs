public class Solution {
    public string MergeAlternately(string word1, string word2) {
        var result = new System.Text.StringBuilder();
        int i = 0;
        int len1 = word1.Length;
        int len2 = word2.Length;

        while ((i < len1) || (i < len2)) {
            if (i < len1) {
                result.Append(word1[i]);
            }
            if (i < len2) {
                result.Append(word2[i]);
            }
            i++;
        }
        return result.ToString();
    }
}
