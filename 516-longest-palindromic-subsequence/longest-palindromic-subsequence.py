class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        #dp[i][j] = longest palindromic subsequence's length for s[i...j] (inclusive)

        #3 options (start from middle char), max them
        #outers match: dp[i][j] = dp[i+1][j-1] + 2
        #ignore leftmost end: dp[i][j] = dp[i+1][j]
        #ignore rightmost end: dp[i][j] = dp[i][j-1]

        #Base Cases
        # "" --> 0 (any empty/negative string (j<i))
        # "x" --> 1 (any single char (i==j))

        dp = [[float('-inf')] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1 #since i,j is inclusive
            for j in range(i):
                dp[i][j] = 0


        for length in range(2,n+1): #2,3,4,5,6,7,8 if n = 8
            for startIndex in range(n-length+1): 
                #0...6(l = 2) 1...7
                #0...5(l = 3)
                #0...4(l = 4)
                #0...3(l = 5)
                #0...2(l = 6)
                #0...1(l = 7)
                #0    (l = 8)
                endIndex = (length-1) + startIndex
                #Option 1
                opt1 = float('-inf')
                if(s[startIndex] == s[endIndex]):
                    opt1 = dp[startIndex+1][endIndex-1] + 2
                
                #Option 2
                opt2 = dp[startIndex+1][endIndex]

                #Option 3
                opt3 = dp[startIndex][endIndex-1]

                dp[startIndex][endIndex] = max(opt1,opt2,opt3)

        return dp[0][n-1]
