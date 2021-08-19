def is_vowel(c: str) -> bool:
    return c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U'


class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s) - 1
        s = list(s)
        while l < r:
            while l < r and not is_vowel(s[l]):
                l += 1
            while r > l and not is_vowel(s[r]):
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
