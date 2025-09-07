class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s

        n = len(s)

        longest = s[0]
        num_char = 0

        possible2 = []

        #Try each character as the middle
        for i, c in enumerate(s):
            if i + 1 < n and c == s[i+1]:
                possible2.append(i)

            if i - num_char >= 0 and i + num_char < n:
                attempt = num_char
                while i - attempt >= 0 and i + attempt < n and s[i - attempt:i] == s[i+1:i + attempt + 1][::-1]:
                    #Palindrome confirmed
                    longest = s[i - attempt:i + attempt + 1]
                    num_char = attempt
                    attempt += 1
                    print(s[i - attempt:i])
                    print(s[i+1:i + attempt + 1])

        print(possible2)

        for i in possible2:
            if i - num_char >= 0 and i + num_char < n:
                #same number of character on each side, two as a center is always longer
                attempt = num_char
                while i - attempt >= 0 and i + attempt < n and s[i - attempt:i] == s[i+2:i + attempt + 2][::-1]:
                    #Palindrome confirmed
                    longest = s[i - attempt:i + attempt + 2]
                    num_char = attempt
                    attempt += 1

        return longest


        

        