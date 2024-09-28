class Solution(object):
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cost.append(0) #Add cost of reaching top
        dp = list(range(0,n+1))

        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,n+1):
            dp[i] = min(dp[i-1],dp[i-2]) + cost[i]
        return dp[n]
        