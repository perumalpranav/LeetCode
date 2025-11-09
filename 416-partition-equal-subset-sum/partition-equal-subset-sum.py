class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        aim = total // 2
        nums = sorted(nums)

        bitset = 1 #O is possible
        for n in nums:
            bitset = bitset | bitset << n #Add num to all 
        return (bitset & 1 << aim) > 0


        