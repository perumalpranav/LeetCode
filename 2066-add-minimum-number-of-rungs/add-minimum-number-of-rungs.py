import math

class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        pos = 0
        added = 0

        for r in rungs:
            if r - pos > dist:
                if (r - pos) % dist == 0:
                    added += (r - pos)/dist - 1
                else:
                    added += math.floor((r - pos)/dist)
            
            pos = r 

        return int(added)