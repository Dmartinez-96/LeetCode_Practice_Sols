class Solution {
    public boolean isSubsequence(String s, String t) {
        int s_ptr = 0;
        // return true if s is empty string
        if (s.length() == 0) {
            return true;
        }
        
        for (int t_ptr = 0; t_ptr < t.length(); t_ptr++) {
            if (s_ptr > (s.length() - 1)) {
                break;
            }
            else if (s.charAt(s_ptr) == t.charAt(t_ptr)) {
                s_ptr++;
            }
        }
        if (s_ptr == s.length()) {
            return true;
        }
        else {
            return false;
        }
    }
}