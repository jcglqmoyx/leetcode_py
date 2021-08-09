from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        f, pointers = [0] * n, [0] * len(primes)
        f[0] = 1
        for i in range(1, n):
            min_value = 10 ** 10
            for j in range(len(primes)):
                tmp = f[pointers[j]] * primes[j]
                if tmp < min_value:
                    min_value = tmp
            f[i] = min_value
            for j in range(len(primes)):
                tmp = f[pointers[j]] * primes[j]
                if tmp == min_value:
                    pointers[j] += 1
        return f[n - 1]
