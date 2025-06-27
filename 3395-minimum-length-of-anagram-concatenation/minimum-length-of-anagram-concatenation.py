from math import gcd
from functools import reduce

class Solution:
    def minAnagramLength(self, s: str) -> int:
        def checkT(trial: int) -> bool:
            sample = sorted(s[0:trial])
            i = trial
            while i < len(s):
                test = sorted(s[i:trial+i])
                if test != sample:
                    return False
                i += trial
            return True

        letters = {}
        for c in s:
            letters[c] = letters.setdefault(c,0) + 1

        all_gcd = reduce(gcd,[*letters.values(),len(s)])

        #Iterate by number of paritions of s rather than length of s
        for g in range(all_gcd, 0, -1):
            if all_gcd % g != 0:
                continue
            t = len(s) // g #length
            print(t)
            if checkT(t):
                return t

        return len(s)


        
