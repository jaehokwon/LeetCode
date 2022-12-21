# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lst = []
        cur = head
        while cur:
            lst.append(cur)
            cur = cur.next
        lst[k-1].val, lst[-k].val = lst[-k].val, lst[k-1].val
        return head