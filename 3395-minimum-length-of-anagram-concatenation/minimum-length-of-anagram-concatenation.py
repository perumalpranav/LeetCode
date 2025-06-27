from math import gcd
from functools import reduce

class Solution:
    def minAnagramLength(self, s: str) -> int:
        def checkT(trial: int) -> bool:
            i = 0
            carryOver = None
            while i < len(s):
                anagramDict = {}
                for letter in s[i:i+trial]:
                    if letter not in anagramDict.keys():
                        anagramDict[letter] = 1
                    else:
                        anagramDict[letter] += 1

                print(f"{carryOver} + {anagramDict}")

                for l in letters:
                    print(l)
                    if l not in anagramDict.keys():
                        return False
                    else:
                        anagramDict[l] -= 1

                print(f"{carryOver} + {anagramDict}")

                sameLetters = True
                numLeftOver = 0
                for key, val in anagramDict.items():
                    if val != 0:
                        numLeftOver += val
                        if carryOver != None:
                            if carryOver[key] != val:
                                print(f"{carryOver} + {anagramDict}")
                                return False
                        
                if (len(letters) + numLeftOver != trial) or not sameLetters:
                    return False

                if carryOver == None:
                    carryOver = copy.deepcopy(anagramDict)

                i += trial

            return True
        
        letters = {}
        for c in s:
            letters[c] = letters.setdefault(c,0) + 1

        attempt = reduce(gcd,[*letters.values(),len(s)])
        if len(s) % attempt == 0:
            attempt = int(len(s)/attempt)

        print(attempt)

        trial = attempt
        while trial < len(s):
            if checkT(trial) == True:
                return trial
            else:
                trial += attempt

        return len(s)


        
