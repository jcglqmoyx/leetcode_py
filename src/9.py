class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x and x % 10 == 0: return False
        y = 0
        while x > y:
            y = y * 10 + x % 10
            x //= 10
        return y // 10 == x or y == x
