class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1, head)
        p = dummy
        while True:
            q = p
            for i in range(k):
                q = q.next
                if not q:
                    break
            if not q:
                break
            a = p.next
            b = a.next
            for i in range(k - 1):
                next = b.next
                b.next = a
                a = b
                b = next
            next = p.next
            p.next = a
            next.next = b
            p = next
        return dummy.next
