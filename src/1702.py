class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        k, n = 0, len(binary)
        while k < n:
            if binary[k] == '1':
                k += 1
            else:
                break
        if k == n:
            return binary
        cnt = 0
        for i in range(k + 1, n):
            if binary[i] == '0':
                cnt += 1
        binary = ['1'] * n
        binary[k + cnt] = '0'
        return ''.join(binary)
