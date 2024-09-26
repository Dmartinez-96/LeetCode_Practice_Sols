class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # index for end of first m elements in num1
        j = n - 1 # index for end of num2
        k = m + n - 1 # Pointer for end of nums1's total length
        while ((i >= 0) and (j >= 0)):
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1
        
        while (j >= 0):
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
