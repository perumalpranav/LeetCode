from collections import deque

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict) #For Hash Lookup
        n = len(s)

        iList = deque([0])
        iSet = {0}
        while len(iList) > 0:
            i = iList.popleft()
            iSet.remove(i)
            for j in range(i+1,n+1):
                if s[i:j] in wordDict:
                    if j == n:
                        return True
                    else:
                        if j not in iSet:
                            iList.append(j)
                            iSet.add(j)
         
        return False
