from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge cases
        if not head or not head.next:
            return head
        # Pointers
        odd = head
        even = head.next
        even_head = even

        # Rearrange nodes
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        # End of odd list is head of even list
        odd.next = even_head

        return head        
