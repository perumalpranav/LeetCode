class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        n = len(favoriteCompanies)
        favoriteCompanies = sorted(list(enumerate(favoriteCompanies)), key=lambda item: len(item[1]))
        
        ans = []

        for i, (originalIndex, companyList) in enumerate(favoriteCompanies):
            sub = False
            for j in range(n-1,i,-1):
                if set(companyList).issubset(set(favoriteCompanies[j][1])):
                    sub = True
                    break

            if not sub:
                ans.append(originalIndex)
        
        return sorted(ans)
            

