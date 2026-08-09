class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        alphabetdict = { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26 }

        alphpos= {k: 0 for k in alphabetdict.values()} #length of best string ending with that num_character

        for _, c in enumerate(s):
            cnum = alphabetdict[c]
            left = max(cnum - k, 1) #num version of character to start at
            right = min(cnum + k, 26) #num version of character to start at

            best = 0
            for anum in range(left,right+1):
                best = max(best, alphpos[anum] + 1)
            
            alphpos[cnum] = best

        return max(alphpos.values())
