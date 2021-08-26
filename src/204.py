import bisect

primes = []
is_prime = [False] * (5 * 10 ** 6 + 1)


def init():
    for i in range(2, len(is_prime)):
        if not is_prime[i]:
            is_prime[i] = True
            primes.append(i)
        j = 0
        while primes[j] * i < len(is_prime):
            is_prime[primes[j] * i] = True
            if i % primes[j] == 0:
                break
            j += 1


class Solution:
    init()

    def countPrimes(self, n: int) -> int:
        p = bisect.bisect_left(primes, n, 0, len(primes))
        return p
