from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        occurences = Counter(nums)
        for k, v in occurences.items():
            if v > n//2:
                return k
        