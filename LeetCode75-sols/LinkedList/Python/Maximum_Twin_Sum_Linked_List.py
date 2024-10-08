from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now slow is in the middle, reverse second half to make sum easier
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        # with prev as the head of the reversed second half, compute twin sums, find max
        max_sum = 0
        first_half = head
        second_half = prev
        while second_half:
            twin_sum = first_half.val + second_half.val
            max_sum = max(max_sum, twin_sum)
            first_half = first_half.next
            second_half = second_half.next
        return max_sum        
