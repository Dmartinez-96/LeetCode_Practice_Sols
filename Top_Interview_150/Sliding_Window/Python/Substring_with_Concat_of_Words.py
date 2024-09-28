class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        # Initialize variables
        word_length = len(words[0])
        word_count = len(words)
        total_length = word_length * word_count
        word_frequency = {}

        # Build the word frequency dictionary
        for word in words:
            if word in word_frequency:
                word_frequency[word] += 1
            else:
                word_frequency[word] = 1

        result = []

        # Iterate over all possible starting points within word_length range
        for i in range(word_length):
            left = i  # Start of the window
            right = i  # End of the window
            current_count = {}  # To store the count of words in the current window
            words_matched = 0  # To track how many words have valid counts in the window

            # Move the window in steps of word_length
            while right + word_length <= len(s):
                # Get the next word from the string
                word = s[right:right + word_length]
                right += word_length

                if word in word_frequency:
                    # Update the count of this word in current window
                    if word in current_count:
                        current_count[word] += 1
                    else:
                        current_count[word] = 1

                    # Check if the word count exceeds the desired frequency
                    if current_count[word] <= word_frequency[word]:
                        words_matched += 1
                    else:
                        # If the count exceeds, we need to move the left pointer
                        while current_count[word] > word_frequency[word]:
                            left_word = s[left:left + word_length]
                            current_count[left_word] -= 1
                            if current_count[left_word] < word_frequency.get(left_word, 0):
                                words_matched -= 1
                            left += word_length

                    # If the number of matched words is equal to the total number of words
                    if right - left == total_length and words_matched == word_count:
                        result.append(left)
                else:
                    # If word is not in word_frequency, reset the window
                    current_count.clear()
                    words_matched = 0
                    left = right

        return result
