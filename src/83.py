class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return None
        dummy = ListNode(-1, head)
        p = head
        while p:
            while p and p.val == head.val:
                p = p.next
            if p:
                head.next = p
                head = head.next
        head.next = p
        return dummy.next
