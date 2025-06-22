import heapq

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
            #Greedy
            #For shop i, items are stored values[i][j] >= values[i][j + 1]

            #Options
            #Pick a shop, Buy the rightmost available item j (not bought before) for the price of values[i][j] * d

            #Combine the different shops together into one big list sorted by price (increasing)
            #Iterate through list and add to the total the (day * price)
            m, n = len(values), len(values[0])

            minheap = []
            for i in range(len(values)):
                heapq.heappush(minheap, (values[i][-1], i))
                values[i].pop(-1)

            totalSpending = 0
            dayCount = 1 #Reverse Order 
            while len(minheap) > 0:
                nextPrice, row = heapq.heappop(minheap)
                print(f"Price {nextPrice}; Day {dayCount}")
                totalSpending += (nextPrice * dayCount)
                if len(values[row]) > 0:
                    heapq.heappush(minheap, (values[row][-1], row))
                    values[row].pop(-1)
                dayCount += 1

            print(minheap)
            return totalSpending
            






        