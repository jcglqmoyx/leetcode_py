num1_19 = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
           'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

num20_90 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
num1000 = ['Billion', 'Million', 'Thousand', '']


def get(x: int) -> str:
    res = ''
    if x >= 100:
        res += num1_19[x // 100 - 1] + ' Hundred '
        x %= 100
    if x >= 20:
        res += num20_90[x // 10 - 2] + ' '
        x %= 10
    if x:
        res += num1_19[x - 1] + ' '
    return res


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        res = ''
        i, j = 10 ** 9, 0
        while num:
            if num >= i:
                res += get(num // i) + num1000[j] + ' '
                num %= i
            i //= 1000
            j += 1
        while res[-1] == ' ':
            res = res[:-1]
        return res
