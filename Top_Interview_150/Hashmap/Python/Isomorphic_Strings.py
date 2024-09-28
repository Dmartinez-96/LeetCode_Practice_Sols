class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Dictionary to map characters in s to characters in t
        s_to_t = {}
        # Dictionary to check if a character in t is already mapped
        t_mapped = {}
        
        # Iterate over characters in both strings
        for char_s, char_t in zip(s, t):
            # If char_s has been seen before
            if char_s in s_to_t:
                # Check if it maps to the correct char_t
                if s_to_t[char_s] != char_t:
                    return False
            else:
                # If char_t is already mapped by some other character
                if char_t in t_mapped:
                    return False
                # Create the mapping
                s_to_t[char_s] = char_t
                t_mapped[char_t] = True
        
        # If we processed all pairs correctly
        return True
