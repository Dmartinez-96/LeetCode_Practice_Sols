class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h_index = 0
        citations.sort(reverse=True)

        for i, c in enumerate(citations):
            if (c >= (i + 1)):
                h_index = 1 + i
            else:
                break
        return h_index
