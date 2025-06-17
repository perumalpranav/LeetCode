import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #Greedily remove the lowest elevation available until you have removed the target value

        def withinBounds(i,j):
            if i < n and i >= 0 and j >= 0 and j < n:
                return True
            else:
                return False

        n = len(grid)
        finished = False
        target = grid[n-1][n-1]
        maxElevation = -1
        
        heap = [[grid[0][0], (0,0)]]
        grid[0][0] = float('inf')

        while finished == False:
            elev, (i, j) = heapq.heappop(heap)
            maxElevation = max(elev,maxElevation)

            if elev == target:
                return maxElevation

            #Right
            if withinBounds(i+1,j) and grid[i+1][j] != float('inf'):
                heapq.heappush(heap,[grid[i+1][j],(i+1,j)])
                grid[i+1][j] = float('inf')
            #Down
            if withinBounds(i,j+1) and grid[i][j+1] != float('inf'):
                heapq.heappush(heap,[grid[i][j+1],(i,j+1)])
                grid[i][j+1] = float('inf')
            #Left
            if withinBounds(i-1,j) and grid[i-1][j] != float('inf'):
                heapq.heappush(heap,[grid[i-1][j],(i-1,j)])
                grid[i-1][j] = float('inf')
            #Up
            if withinBounds(i,j-1) and grid[i][j-1] != float('inf'):
                heapq.heappush(heap,[grid[i][j-1],(i,j-1)])
                grid[i][j-1] = float('inf')