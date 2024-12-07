class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        even = 0  # max sum ending with even length subsequence
        odd = 0   # max sum ending with odd length subsequence
        
        for num in nums:
            # Two options for even length:
            # 1. Keep previous even sum
            # 2. Add current num to previous odd sum
            new_even = max(even, odd + num)
            
            # Two options for odd length:
            # 1. Keep previous odd sum
            # 2. Subtract current num from previous even sum
            new_odd = max(odd, even - num)
            
            even = new_even
            odd = new_odd
        
        return even