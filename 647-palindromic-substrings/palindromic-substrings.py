class Solution:
    def countSubstrings(self, s: str) -> int:
        numPalindromes = len(s)
        palindromes = set(c for c in s) #add in all single characters
        
        for i in range(len(s)-1): #add in all valid pairs
            if s[i] == s[i+1]:
                palindromes.add(s[i:i+2])
                numPalindromes += 1

        l = 3
        while l <= len(s):
            for i in range(len(s)-l+1):
                j = i + l - 1
                if s[i] == s[j] and s[i+1:i+l-1] in palindromes:
                    palindromes.add(s[i:i+l])
                    numPalindromes += 1
            l+=1

        return numPalindromes
        

        
