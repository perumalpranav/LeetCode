class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j):
            if i < m and i >= 0 and j >= 0 and j < n and grid[i][j] == 1:
                grid[i][j] = 0
                return dfs(i-1,j) + dfs(i+1,j) + dfs(i,j+1) + dfs(i,j-1) + 1
            else:
                return 0



        maxArea = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area = dfs(i,j)#DFS Calculate island and change the values
                    if area > maxArea:
                        maxArea = area
        
        return maxArea
        