class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to store the frequency of each character in magazine
        char_count = {}
        
        # Count the occurrences of each character in the magazine
        for char in magazine:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Check if ransomNote can be constructed
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False  # Not enough characters in the magazine
            char_count[char] -= 1  # Use one character
        
        # If we successfully used all characters from ransomNote
        return True
