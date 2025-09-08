from collections import deque
import math

class Solution:  
    def convert(self, s: str, numRows: int) -> str:
        #ith row, jth column

        n = len(s)

        if n == 1 or n == 2 or numRows == 1:
            return s

        cycleLen = numRows + numRows - 2

        cycles = [deque(s[i:i+cycleLen]) for i in range(0, n, cycleLen)]
        ans = ""

        #Take first character of each cycle
        for c in cycles:
            ans = f"{ans}{c.popleft()}"

        #Take first and last character of each full cycle until none are left
        noneLeft = False
        passCompleted = 1
        while not noneLeft:
            countNone = 0
            print("Loop Start")
            for i, c in enumerate(cycles):
                if not i == len(cycles) - 1:
                    if len(c) > 0:
                        ans=f"{ans}{c.popleft()}"
                    else:
                        countNone += 1
                    if len(c) > 0:
                        ans=f"{ans}{c.pop()}"
                else:
                    if len(c) > 0:
                        ans=f"{ans}{c.popleft()}"
                    else:
                        countNone += 1
                    if len(c) > 0:
                        #Check if the row is correct
                        print(f"len: {len(c)} expected: {cycleLen - 2 * passCompleted}")

                        if len(c) == cycleLen - 2 * passCompleted:
                            ans=f"{ans}{c.pop()}"
            print("Loop End")
            passCompleted += 1
            
            if countNone == len(cycles):
                noneLeft = True

        return ans


        