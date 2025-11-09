from collections import deque

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b):
            b = b.zfill(len(a))
        elif len(b) > len(a):
            a = a.zfill(len(b))

        result = deque([])
        carry = '0'
        for ac, bc in zip(reversed(a),reversed(b)):
            if ac == '1' and bc == '1':
                result.appendleft(carry)
                carry = '1'
            elif ac == '0' and bc == '0':
                result.appendleft(carry)
                carry = '0'
            else:
                if carry == '1':
                    result.appendleft('0')
                    carry = '1'
                else:
                    result.appendleft('1')
                    carry = '0'

        if carry != '0':
            result.appendleft('1')

        r = ''.join(result)
        return r

        