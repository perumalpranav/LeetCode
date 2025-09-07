class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #ith row, jth column

        n = len(s)

        if n == 1 or n == 2 or numRows == 1:
            return s

        n = len(s)


        cycleLen = numRows + numRows - 2
        num_cycles = n//cycleLen + 1
        col_per_cycle = 1 + numRows - 2
        num_columns = num_cycles * col_per_cycle


        matrix = [['?'] * (num_columns) for _ in range(numRows)]

        previ, prevj = 0, 0
        i, j = 1, 0
        
        matrix[previ][prevj] = s[0]
        matrix[i][j] = s[1]

        def nextIndex(previ, prevj, i, j):
            if previ == i - 1:
                #last direction was downward
                if i == numRows-1:
                    #Go diagonally up
                    return (i-1, j+1)
                else:
                    #Go down again
                    return (i+1, j)
            elif previ == i + 1 and prevj == j - 1:
                #last direction was diagonally up
                if i == 0:
                    #Go down now
                    return (i+1, j)
                else:
                    #Continue diagonally up
                    return (i-1, j+1)
            else:
                #SOMETHING WENT WRONG
                print("OHHHHNOOOOOOO")


        for c in s[2:]:
            nexti, nextj = nextIndex(previ, prevj, i, j)
            matrix[nexti][nextj] = c


            previ, prevj = i, j
            i, j = nexti, nextj

        ans = ""
        for i in range(numRows):
            for j in range(num_columns):
                if matrix[i][j] != '?':
                    ans = f"{ans}{matrix[i][j]}"

        for m in matrix:
            for e in m:
                print(e, end="")
            print()

        return ans

        


        