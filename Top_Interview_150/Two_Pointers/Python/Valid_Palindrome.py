class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatStr = ''.join([ch for ch in s.lower() if ch.isalnum()])
        return formatStr == formatStr[::-1]
