class Solution {
    public int compress(char[] chars) {
        int n = chars.length;
        if (n == 1) {
            return 1;
        }
        int j = 0;
        int count = 1;
        for (int i = 0; i < chars.length; i++) {
            count = 1;
            while ((i < (n - 1)) && (chars[i] == chars[i+1])) {
                count += 1;
                i += 1;
            }

            chars[j] = chars[i];
            j += 1;

            if (count > 1) {
                String countStr = Integer.toString(count);
                for (int k = 0; k < countStr.length(); k++) {
                    chars[j] = countStr.charAt(k);
                    j += 1;
                }
            }
        }
    return j;
    }
}