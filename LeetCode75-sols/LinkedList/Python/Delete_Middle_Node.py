# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Edge case:
        if not head or not head.next:
            return None
        
        # Pointers
        slow = head
        fast = head
        prev = None # Node before slow

        # Traverse list to middle node
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        # Delete the middle node
        prev.next = slow.next
        return head
