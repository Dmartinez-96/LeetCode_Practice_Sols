class Solution {
public:
    string reverseVowels(string s) {
        string s2 = "";
        string vowel_str = "";
        for (int i = 0; i < s.length(); i++) {
            if (checker(s[i])) {
                vowel_str += s[i];
            }
        }
        int cnt = vowel_str.length();
        for (int j = 0; j < s.length(); j++) {
            if (checker(s[j])) {
                s2 += vowel_str[cnt-1];
                cnt--;
            }
            else {
                s2 += s[j];
            }
        }
        return s2;
    }

    bool checker(char s)
    {
        if (s=='a' | s=='e' | s=='i' | s=='o' | s=='u' | s=='A' | s=='E' | s=='I' | s=='O' | s=='U') {
            return true;
        }
        return false;
    }
};