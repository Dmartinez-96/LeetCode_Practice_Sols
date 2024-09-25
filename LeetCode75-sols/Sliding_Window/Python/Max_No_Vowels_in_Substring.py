class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        isVowel = lambda x: x in 'aeiou' # Lambda bool function for getting vowels
        sm = mx = sum(map(isVowel, s[:k])) # First k characters of s
        for i in range(len(s) - k):
            sm += isVowel(s[i+k]) - isVowel(s[i]) # Updates with next character, removing earliest character in grouping of k
            if (sm > mx):
                mx = sm
        return mx
