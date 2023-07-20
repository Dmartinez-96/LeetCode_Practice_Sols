class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        if n==1:
            return 1
        # i is left pointer, j is right ptr
        i,j = 0,0
        while i<n:
            count = 1
            while ((i < (n-1)) and (chars[i] == chars[i+1])):
                count += 1
                i += 1
            
            # Set left most entry in final chars array then increment j,i
            chars[j] = chars[i]
            j += 1
            i += 1

            # Input length of compressed characters in chars as string
            if count > 1:
                for k in range(len(str(count))):
                    chars[j] = str(count)[k]
                    j += 1

        return j