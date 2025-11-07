class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []

        summ = []
        integer = 2
        
        while integer <= finalSum and finalSum > 0:
            finalSum -= integer
            summ.append(integer)
            integer += 2
        
        if finalSum == 0:
            return summ
        else:
            last = summ.pop()
            summ.append(finalSum + last)
            return summ
        
        