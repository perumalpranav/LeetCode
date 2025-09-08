from collections import deque
import math

class Solution:  
    def convert(self, s: str, numRows: int) -> str:
        #ith row, jth column

        n = len(s)

        if n == 1 or n == 2 or numRows == 1:
            return s

        sub = [[] for _ in range(numRows)]

        rowNum = 0
        direction = 1
        for c in s:
            if rowNum == numRows:
                direction = -1
                rowNum = numRows - 2
            elif rowNum == -1:
                direction = 1
                rowNum = 1

            print(rowNum)
            sub[rowNum].append(c)
            rowNum += direction
            
        for i, s in enumerate(sub):
            sub[i] = "".join(s)

        return "".join(sub)


        