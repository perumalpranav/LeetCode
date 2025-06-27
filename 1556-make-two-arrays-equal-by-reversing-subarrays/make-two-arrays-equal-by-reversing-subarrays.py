class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        elements = {}
        for e in arr:
            elements[e] = elements.setdefault(e, 0) + 1

        for e in target:
            if e in elements.keys():
                elements[e] -= 1
            else:
                return False

        for val in elements.values():
            if val != 0:
                return False
        
        return True