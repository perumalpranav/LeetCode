class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0


        new = list(str(x))

        #Non-reversed operations - separated because only .pop() is O(1), not .pop(0), and we have to reverse anyway
        while new[-1] == '0':
            new.pop()

        negative = False
        if new[0] == '-':
            new.append('-')
            negative = True

        #Reverse
        new = new[::-1]

        #Reversed operations
        if negative:
            new.pop()

        new = "".join(new)
        new = int(new)

        if new <= (2**31 - 1) and new >= -1 * (2**31):
            return new
        else:
            return 0
        
        