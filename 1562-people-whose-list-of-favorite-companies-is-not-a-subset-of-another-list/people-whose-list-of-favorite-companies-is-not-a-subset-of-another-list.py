class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        favoriteCompanies = sorted(list(enumerate(favoriteCompanies)), key=lambda item: len(item[1]))
        
        companyHash = {}
        index = 0
        bitList = []

        for originalIndex, companyList in favoriteCompanies:
            bitmask = 0
            for c in companyList:
                if c not in companyHash:
                    companyHash[c] = index
                    index += 1
                    
                mask = 1 << companyHash[c]
                bitmask |= mask

            bitList.append((originalIndex, bitmask))

        ans = []
        i = 0
        j = n-1

        for i in range(n):
            sub = False
            for j in range(i+1, n):
                if (bitList[i][1] & bitList[j][1]) == bitList[i][1]:
                    sub = True
                    break
            if not sub:
                ans.append(bitList[i][0])

        return sorted(ans)
            

