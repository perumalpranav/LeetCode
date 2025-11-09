class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        if not len(s):
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        s = s.lstrip('0')
        if not len(s) > 0:
            return 0

        num = []
        for c in s:
            if c.isnumeric():
                num.append(c)
            else:
                break

        if not len(num):
            return 0

        num = sign * int(''.join(num))

        if num > (2**31 - 1):
            return (2**31 - 1)
        elif num < (-1 * 2 ** 31):
            return (-1 * 2 ** 31)
        
        return num
        