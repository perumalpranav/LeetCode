from math import gcd
from functools import reduce

class Solution:
    def minAnagramLength(self, s: str) -> int:
        letters = set()
        for c in s:
            letters.add(c)
        
        #len(letters) minimum possible length of t

        def checkT(trial: int) -> bool:
            sample = sorted(s[0:trial])
            i = trial
            while i < len(s):
                test = sorted(s[i:trial+i])
                if test != sample:
                    return False
                i += trial
            return True

        

        lo = len(letters)
        hi = len(s)

        while lo < hi:
            if len(s) % lo != 0:
                lo += 1
                continue
            if checkT(lo):
                return lo
            lo += 1

        return lo