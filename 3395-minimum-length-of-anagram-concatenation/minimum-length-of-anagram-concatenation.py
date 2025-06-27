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

        attempt = reduce(gcd,[*letters.values(),len(s)])
        if len(s) % attempt == 0:
            attempt = int(len(s)/attempt)

        print(attempt)

        trial = max(attempt, len(letters))
        while trial < len(s):
            if checkT(trial) == True:
                return trial
            else:
                trial += attempt

        return len(s)


        