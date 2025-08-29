class Solution:
    def minimumSum(self, num: int) -> int:
        #Minimum sum, put the biggest numbers in the smallest positions
        chars = list(str(num))
        chars = sorted(chars, reverse = True)

        decimal = 1
        totalsum = 0
        while len(chars) > 0:
            totalsum += decimal * int(chars.pop(0))
            totalsum += decimal * int(chars.pop(0))
            decimal *= 10

        return totalsum
