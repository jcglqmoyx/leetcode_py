class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, node: ListNode) -> ListNode:
        prev = None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
        return prev

    def isPalindrome(self, head: ListNode) -> bool:
        fast = slow = head
        while fast and fast.next and fast.next.next:
            fast = not fast.next
            slow = slow.next
        l, r = head, self.reverse(slow.next)
        while l and r:
            if l.val != r.val:
                return False
            l, r = l.next, r.next
        return True
