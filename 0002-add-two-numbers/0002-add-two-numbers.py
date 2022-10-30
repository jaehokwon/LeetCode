class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode(0, None)
        node_cur = None
        carry = False

        while l1 or l2 or carry:
            num = 0

            if l1:
                num += l1.val
                l1 = l1.next
            
            if l2:
                num += l2.val
                l2 = l2.next
            
            if carry:
                num += 1
            
            if num//10 > 0:
                carry = True
                num %= 10
            else:
                carry = False
            
            if not node_cur:
                node_cur = node
                node_cur.val = num
            else:
                node_cur.next = ListNode(num, None)
                node_cur = node_cur.next

        return node