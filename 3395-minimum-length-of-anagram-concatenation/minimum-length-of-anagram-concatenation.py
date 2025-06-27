from math import gcd
from functools import reduce

class Solution:
    def minAnagramLength(self, s: str) -> int:
        def checkT(trial: int) -> bool:
            sample = sorted(s[0:trial])
            for i in range(trial, len(s), trial):
                test = sorted(s[i:trial+i])
                if test != sample:
                    return False
            return True

        letters = {}
        for c in s:
            letters[c] = letters.setdefault(c,0) + 1

        attempt = reduce(gcd,[*letters.values(),len(s)])
        if len(s) % attempt == 0:
            attempt = int(len(s)/attempt)


        trial = max(attempt, len(letters))
        for i in range(trial, len(s), attempt):
            if checkT(i) == True:
                return i

        return len(s)


        