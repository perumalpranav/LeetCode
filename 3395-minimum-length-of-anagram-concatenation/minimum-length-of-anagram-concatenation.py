import copy

class Solution:
    def minAnagramLength(self, s: str) -> int:
        letters = set()
        for c in s:
            letters.add(c)
        
        #len(letters) minimum possible length of t

        #String t
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