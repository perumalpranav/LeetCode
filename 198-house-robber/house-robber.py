class Solution(object):
    def rob(self, nums):
        n = len(nums)
        dp = list(range(0,n+1))
        dp[0] = 0
        dp[1] = nums[0]
        if n == 1:
            return dp[1]

        for i in range(2,n+1):
            dp[i] = max((dp[i-2]+nums[i-1]),dp[i-1])
        return dp[n]
        