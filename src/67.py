class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                sum = int(a[i]) + int(b[j]) + carry
                res.append(str(sum % 2))
                carry = sum // 2
                i -= 1
                j -= 1
            elif i >= 0:
                sum = int(a[i]) + carry
                res.append(str(sum % 2))
                carry = sum // 2
                i -= 1
            else:
                sum = int(b[j]) + carry
                res.append(str(sum % 2))
                carry = sum // 2
                j -= 1
        if carry:
            res.append('1')
        res.reverse()
        return ''.join(res)
