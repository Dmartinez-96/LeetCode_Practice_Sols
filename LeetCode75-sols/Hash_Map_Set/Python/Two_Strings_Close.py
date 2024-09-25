class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Check that string lengths are the same
        if (len(word1) != len(word2)):
            return False
        # Check that same unique characters are in the two strings
        if (set(word1) != set(word2)):
            return False
        # Count character frequency
        chars_word1 = {}
        chars_word2 = {}
        for char in word1:
            chars_word1[char] = True
        for char in word2:
            chars_word2[char] = True
        freq_word1 = {}
        freq_word2 = {}

        for char in word1:
            freq_word1[char] = freq_word1.get(char, 0) + 1
        for char in word2:
            freq_word2[char] = freq_word2.get(char, 0) + 1
        counts_word1 = list(freq_word1.values())
        counts_word2 = list(freq_word2.values())

        counts_word1.sort()
        counts_word2.sort()

        return (counts_word1 == counts_word2)
