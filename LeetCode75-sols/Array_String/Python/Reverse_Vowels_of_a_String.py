class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s2 = ''
        vowel_str = ''
        for i in range(len(s)):
            if s.lower()[i] in vowels:
                vowel_str += s[i]
        vowel_str = vowel_str[::-1]
        cnt = 0
        for i in range(len(s)):
            if s.lower()[i] in vowels:
                s2 += vowel_str[cnt]
                cnt += 1
            else:
                s2 += s[i]
        return s2