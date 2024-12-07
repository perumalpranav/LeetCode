class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Base case: If the string is empty, there are no decodings
        if n == 0:
            return 0
        
        # dp[i] represents the number of decodings for the substring s[0:i]
        dp = [0] * (n + 1) 
        
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1):
            # Option 1: Decode the current character as a single character (not '0')
            singledigit = dp[i-1] if s[i - 1] != '0' else 0
            
            # Option 2: Decode the last two characters as a two-digit number (between 10 and 26)
            doubledigit = dp[i-2] if '10' <= s[i - 2:i] <= '26' else 0

            dp[i] = singledigit + doubledigit
        
        return dp[n]
