class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        s.add(n)
        while n != 1:
            tmp, sum = n, 0
            while tmp:
                sum += (tmp % 10) * (tmp % 10)
                tmp //= 10
            if sum in s:
                return False
            s.add(sum)
            n = sum
        return True
