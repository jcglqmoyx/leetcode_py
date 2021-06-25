class Solution:
    def isValid(self, s: str) -> bool:
        d = {')': '(', ']': '[', '}': '{'}
        stack = []
        for c in s:
            if c in d:
                if not stack or stack[-1] != d[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return not stack
