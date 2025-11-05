class Solution:
    def countSubstrings(self, s: str) -> int:
        numPalindromes = len(s)
        n = len(s)
        dp = [[False] * (n+1) for _ in range(n+1)]
        
        for i in range(n):
            dp[i][i] = True #No letters
            dp[i][i+1] = True #One letter

        l = 2
        while l <= len(s):
            for i in range(len(s)-l+1):
                j = i + l - 1
                if s[i] == s[j] and dp[i+1][i+l-1]:
                    dp[i][i+l] = True
                    numPalindromes += 1
            l+=1

        return numPalindromes
        

        
