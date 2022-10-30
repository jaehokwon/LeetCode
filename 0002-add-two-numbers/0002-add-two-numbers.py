# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.convertNumberToNode(self.convertNodeToNumber(l1) + self.convertNodeToNumber(l2))
    
    def convertNodeToNumber(self, l: Optional[ListNode]) -> int:
        node = l
        list_num = []

        while node is not None:
            list_num.append(node.val)
            node = node.next
        
        list_num.reverse()
        return int(''.join([str(i) for i in list_num]))
    
    def convertNumberToNode(self, num: int) -> Optional[ListNode]:
        node = None
        node_last = None

        while num > 0:
            node_cur = ListNode(num%10, None)

            if node is None:
                node = node_cur
            else:
                node_last.next = node_cur

            num = num//10
            node_last = node_cur
        
        return node if node else ListNode(0, None)