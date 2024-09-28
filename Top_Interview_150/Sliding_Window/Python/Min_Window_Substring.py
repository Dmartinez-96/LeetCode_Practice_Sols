class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        required = {}
        for char in t:
            if char in required:
                required[char] += 1
            else:
                required[char] = 1

        # Number of unique characters in t that need to be present in the window.
        required_char_count = len(required)
        window_count = {}
        have = 0  # Number of unique characters that match their frequency in window
        left = 0
        result = float("inf"), None, None  # length, start, end

        for right in range(len(s)):
            char = s[right]
            
            # Add current character to window_count
            if char in window_count:
                window_count[char] += 1
            else:
                window_count[char] = 1

            # Check if current window has enough of char to satisfy the requirement
            if char in required and window_count[char] == required[char]:
                have += 1

            # Try to shrink the window from the left if all required characters are in the window
            while have == required_char_count:
                # Update result if this window is smaller than the previously recorded one
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)

                # Try to move the left pointer to shrink the window
                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in required and window_count[left_char] < required[left_char]:
                    have -= 1

                left += 1

        # If result[0] is still infinity, it means no valid window was found
        if result[0] == float("inf"):
            return ""

        # Return the smallest window substring
        return s[result[1]:result[2] + 1]
