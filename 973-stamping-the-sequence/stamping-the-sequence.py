class Solution:
    def removalPossible(self, stamp: str, target: str) -> bool:
        for c1, c2 in zip(stamp, target):
            if c2 != "?" and c1 != c2:
                return False
        return True
    
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        count = []
        n, m = len(target), len(stamp)
        turns = 0

        if stamp not in target:
            return count


        #Strategy: Unstamp the target one by one

        #n-m+1 is all possible places one can stamp
        stampLocs = set([i for i in range(n-m+1)])

        blank = "?" * m
        while turns < n * 10:
            tmp = turns
            for loc in stampLocs.copy():
                if target[loc:loc+m] != blank and self.removalPossible(stamp, target[loc:loc+m]):
                    #Removal operation (because string concatenation is slow in Python)
                    target = list(target)
                    for j in range(loc,loc+m):
                        target[j] = "?"
                    target = ''.join(target)

                    count.append(loc)
                    stampLocs.remove(loc)
                    turns += 1

            #If target is completely removed
            allRemoved = True
            for i in range(n):
                if target[i] != "?":
                    allRemoved = False
                    break
        
            if allRemoved:
                #reverse the order and return due to 'unstamping' process
                return count[::-1]

            #If no removal is possible and target is not completely removed
            if turns == tmp:
                return []

        print("ddd")
        return []


            
            