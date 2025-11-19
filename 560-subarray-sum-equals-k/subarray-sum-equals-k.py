from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefixes = defaultdict(int)
        prefixes[0] = 1
        pre = 0
        for i in range(n):
            pre += nums[i]
            if (pre - k) in prefixes:
                count += prefixes[pre-k]
            prefixes[pre] += 1
                
        return  count

            
        return count
