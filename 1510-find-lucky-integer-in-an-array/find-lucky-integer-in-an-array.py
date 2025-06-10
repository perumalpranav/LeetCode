class Solution:
    def findLucky(self, arr: List[int]) -> int:
        frequency = {}
        for num in arr:
            if num in frequency.keys():
                frequency[num] = frequency[num] + 1
            else:
                frequency[num] = 1

        maxL = -1
        for key, val in frequency.items():
            if key > maxL and key == val:
                maxL = key
        
        return maxL