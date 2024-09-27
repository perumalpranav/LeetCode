import math

class Solution(object):
    def numSquares(self, n):
        dp = list(range(0,n+1))
        dp[0] = 0
        dp[1] = 1
        for i in range(2,n+1):
            top = int(math.sqrt(n))
            mini = 300000
            for j in range(1,top+1):
                if (dp[(i-(j**2))] + 1) < mini:
                    mini = dp[(i-(j**2))] + 1
            dp[i] = mini
        return dp[n]