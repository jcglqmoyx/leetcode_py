class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x = -x
        y = 0
        while x:
            y = y * 10 + x % 10
            x //= 10
        if y < -2 ** 31 or y > 2 ** 31: return 0
        return y if not is_negative else -y
