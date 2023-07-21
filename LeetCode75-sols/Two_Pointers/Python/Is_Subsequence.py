class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_ptr = 0
        # Return True if s is empty string
        if (len(s)==0):
            return True

        for t_ptr in range(len(t)):
            if (s_ptr > (len(s) - 1)):
                break
            elif (s[s_ptr] == t[t_ptr]):
                s_ptr += 1

        if (s_ptr == len(s)):
            return True
        else:
            return False