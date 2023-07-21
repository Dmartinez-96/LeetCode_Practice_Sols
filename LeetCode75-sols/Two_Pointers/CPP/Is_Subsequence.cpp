class Solution {
public:
    bool isSubsequence(string s, string t) {
        int s_ptr = 0;
        // Return True if s is empty string
        if (s.size() == 0) {
            return true;
        }

        for (int t_ptr = 0; t_ptr < t.size(); t_ptr++) {
            if (s_ptr > (s.size() - 1)) {
                break;
            }
            else if (s[s_ptr] == t[t_ptr]) {
                s_ptr++;
            }
        }
        if (s_ptr == s.size()) {
            return true;
        }
        else {
            return false;
        }
    }
};