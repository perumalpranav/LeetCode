from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letterDict = Counter(ransomNote)
        for l in magazine:
            if not len(letterDict) > 0:
                return True

            if l in letterDict:
                letterDict[l] -= 1
                if letterDict[l] <= 0:
                    del letterDict[l]

        if not len(letterDict) > 0:
            return True
        else:
            return False
            
