class Solution(object):
    def maxUncrossedLines(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        n = len(nums1)
        m = len(nums2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

        #3 cases (get max of all)
        #Found matching, 1 + subsequence dp[i-1][j-1]
        #Did not find matching, subsequence dp[i][j-1]
        #Did not find matching, subsequence dp[i-1][j]
        
        for i in range(1,n+1):
            for j in range(1,m+1):
                if(nums1[i-1] == nums2[j-1]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                opt2 = dp[i-1][j]
                opt3 = dp[i][j-1]
                dp[i][j] = max(dp[i][j],opt2,opt3)
        
        return dp[n][m]
                
