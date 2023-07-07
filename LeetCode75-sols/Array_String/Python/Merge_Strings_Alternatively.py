class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        mergestr = ''
        for i in range(min([len(word1), len(word2)])):
            mergestr += word1[i]
            mergestr += word2[i]
        mergestr += word1[min([len(word1), len(word2)]):]
        mergestr += word2[min([len(word1), len(word2)]):]
        return mergestr