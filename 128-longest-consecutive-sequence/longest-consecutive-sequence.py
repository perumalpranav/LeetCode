from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = (set(nums))

        best = 0
        for n in nums_set:
            if (n-1) not in nums_set:
                chain = 1
                while n + chain in nums_set:
                    chain += 1
                best = max(chain, best)
        
        return best