class Solution {
public:
    int compress(vector<char>& chars) {
        if (size(chars) == 1) {
            return 1;
        }
        int j = 0;
        int count = 1;
        for (int i = 0; i < size(chars); i++) {
            count = 1;
            while ((i < (size(chars) - 1)) && (chars[i] == chars[i+1])) {
                count += 1;
                i += 1;
            }

            chars[j] = chars[i];
            j += 1;

            if (count > 1) {
                for (int k = 0; k < to_string(count).length();  k++) {
                    chars[j] = to_string(count)[k];
                    j += 1;
                } 
            }
        }
        return j;
    }
};