class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n = len(days)
        dp = [float('inf')] * (days[-1] + 1)  # Create DP array based on the last travel day

        dp[0] = 0  # Base case: 0 cost for day 0
        
        for day in range(1, days[-1] + 1):
            # If this is not a travel day, cost is same as previous day
            if day not in days:
                dp[day] = dp[day - 1]
                continue
            
            # Try 1-day, 7-day, and 30-day passes
            dp[day] = min(
                dp[max(0, day - 1)] + costs[0],    # 1-day pass
                dp[max(0, day - 7)] + costs[1],    # 7-day pass
                dp[max(0, day - 30)] + costs[2]    # 30-day pass
            )
        
        return dp[days[-1]]