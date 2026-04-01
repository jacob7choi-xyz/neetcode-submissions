# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, dummy

        # Creates the gap between fast node and slow node
        for i in range(n):
            fast = fast.next

        # Move both together now to get fast to end where fast hits None
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Now we need to skip over that nth node which is slow.next
        slow.next = slow.next.next
        
        return dummy.next



