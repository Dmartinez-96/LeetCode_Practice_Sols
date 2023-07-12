class Solution:
    def reverseWords(self, s: str) -> str:
        rev_words = s.split()
        rev_words = rev_words[::-1]
        rev_s = ''
        for word in rev_words:
            rev_s += word
            rev_s += ' '
        rev_s = rev_s.rstrip()
        return rev_s