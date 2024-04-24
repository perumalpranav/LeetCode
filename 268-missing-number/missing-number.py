class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = (len(nums) * (len(nums)+1))/2
        i = 0
        while(i < len(nums)):
            sum-=nums[i]
            i+=1
        return sum
        