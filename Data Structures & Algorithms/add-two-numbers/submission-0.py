# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy, carry = ListNode(), 0

        current = dummy
        while l1 or l2 or carry:
            val1, val2 = l1.val if l1 else 0, l2.val if l2 else 0
            sum = carry + val1 + val2
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            l1, l2 = l1.next if l1 else None, l2.next if l2 else None
        return dummy.next