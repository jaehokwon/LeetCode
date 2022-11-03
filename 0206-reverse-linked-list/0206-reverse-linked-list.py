# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = ListNode(0, None)
        self.last_node = res
        
        def searchNode(n: ListNode):
            if n and n.next:
                searchNode(n.next)
            self.last_node.next = ListNode(n.val)
            self.last_node = self.last_node.next
        
        searchNode(head)
        return res.next