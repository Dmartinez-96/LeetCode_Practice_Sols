class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [] # Holds all lines
        current_words = [] # Holds current line
        current_length = 0 # For length of current line
        
        i = 0
        while (i < len(words)):
            word = words[i]
            if ((current_length + len(current_words) + len(word)) <= maxWidth):
                current_words.append(word)
                current_length += len(word)
                i += 1
            else:
                # Justify current line
                line = ''
                number_of_words = len(current_words)
                if number_of_words == 1:
                    line = current_words[0] + ' ' * (maxWidth - current_length)
                else:
                    total_spaces = maxWidth - current_length
                    number_of_slots = number_of_words - 1
                    min_spaces = total_spaces // number_of_slots
                    extra_spaces = total_spaces % number_of_slots
                    for j in range(number_of_slots):
                        line += current_words[j]
                        spaces_to_add = min_spaces + (1 if j < extra_spaces else 0)
                        line += ' ' * spaces_to_add
                    line += current_words[-1] # Adds last word
                lines.append(line)
                current_words = []
                current_length = 0
        last_line = ' '.join(current_words)
        last_line += ' ' * (maxWidth - len(last_line))
        lines.append(last_line)

        return lines
