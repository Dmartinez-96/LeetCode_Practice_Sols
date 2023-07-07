class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # GCD routine by Euler's method
        def hcf(a, b):
            if(b == 0):
                return a
            else:
                return hcf(b, a % b)
        # USING STR1 + STR2 == STR2 + STR1 IFF THERE IS A COMMON DIVISOR
        if (str1 + str2 != str2 + str1):
            return ""
        return str1[0:hcf(len(str1), len(str2))]