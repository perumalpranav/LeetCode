class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def indexRotations(i,j):
            #90 degrees clockwise
            return j, n - 1 - i

        rot0 = True
        rot90 = True
        rot180 = True
        rot270 = True

        for i, row in enumerate(mat):
            for j, cell in enumerate(mat[0]):
                if not rot0 and not rot90 and not rot180 and not rot270:
                    return False

                if rot0:
                    contVal = (mat[i][j] == target[i][j])
                    if contVal == False:
                        rot0 = False
                if rot90:
                    rI, rJ = indexRotations(i,j)
                    contVal = (mat[i][j] == target[rI][rJ])
                    if contVal == False:
                        rot90 = False
                if rot180:
                    rI, rJ = indexRotations(*indexRotations(i,j))
                    contVal = (mat[i][j] == target[rI][rJ])
                    if contVal == False:
                        rot180 = False
                if rot270:
                    rI, rJ = indexRotations(*indexRotations(*indexRotations(i,j)))
                    contVal = (mat[i][j] == target[rI][rJ])
                    if contVal == False:
                        rot270 = False

        if rot0 or rot90 or rot180 or rot270:
            return True
        
        return False

                
        