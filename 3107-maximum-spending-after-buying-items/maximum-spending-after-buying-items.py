class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
            #Greedy
            #For shop i, items are stored values[i][j] >= values[i][j + 1]

            #Options
            #Pick a shop, Buy the rightmost available item j (not bought before) for the price of values[i][j] * d

            #Combine the different shops together into one big list sorted by price (increasing)
            #Iterate through list and add to the total the (day * price)

            def compareFirstElements() -> int:
                maxRow = -1
                maxVal = float('-inf')
                
                for i in range(len(values)):
                    if len(values[i]) > 0:
                        if values[i][0] > maxVal:
                            maxRow = i
                            maxVal = values[i][0]
                
                if maxRow != -1:
                    values[maxRow].pop(0)

                return maxVal

            totalSpending = 0
            dayCountdown = len(values[0] * len(values)) #Reverse Order (must be calculated before the first compareFirstElements Call)
            nextPrice = compareFirstElements()
            while nextPrice != float('-inf'):
                totalSpending += (nextPrice * dayCountdown)
                nextPrice = compareFirstElements()
                dayCountdown -= 1

            return totalSpending
            






        