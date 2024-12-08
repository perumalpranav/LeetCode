class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        n = len(s1)
        m = len(s2)
        dp = [[0] * (m+1) for _ in range(n+1)]

        #3 options (min all)
        #same character --> use dp[i-1][j-1]
        #diff character --> use dp[i-1][j] + asciival(s1[i-1])
        #diff character --> use dp[i][j-1] + asciival(s2[j-1])

        for i in range(1,n+1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])

        for j in range(1,m+1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1,n+1):
            for j in range(1,m+1):
                opt1 = float('inf')
                if s1[i-1] == s2[j-1]:
                    opt1 = dp[i-1][j-1]
                
                opt2 = dp[i-1][j] + ord(s1[i-1])
                opt3 = dp[i][j-1] + ord(s2[j-1])
                dp[i][j] = min(opt1,opt2,opt3)
        
        print(dp)
        return dp[n][m]

        