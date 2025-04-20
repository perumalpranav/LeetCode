class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        elements = {}
        for e in arr:
            if e in elements.keys():
                elements[e] += 1
            else:
                elements[e] = 1

        for e in target:
            if e in elements.keys():
                elements[e] -= 1
            else:
                return False

        for val in elements.values():
            if val != 0:
                return False
        
        return True