class Solution(object):
    def climbStairs(self, n):
        dp = list(range(n+1))
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]