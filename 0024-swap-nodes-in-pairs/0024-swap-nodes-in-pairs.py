# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        first = head
        head = second = head.next
        parent = None
        while first and second:
            first.next, second.next = second.next, first
            if parent:
                parent.next = second
            first = first.next
            if first:
                parent = second.next
                second = first.next
        return head