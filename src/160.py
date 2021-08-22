class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a, b = headA, headB
        flag_a = flag_b = False
        while headA and headB and headA != headB:
            headA = headA.next
            headB = headB.next
            if not headA:
                if flag_a:
                    return None
                else:
                    flag_a = True
                    headA = b
            if not headB:
                if flag_b:
                    return None
                else:
                    flag_b = True
                    headB = a
        return headA
