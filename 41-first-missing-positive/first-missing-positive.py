class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if(nums[i] > 0 and nums[i] <= len(nums) and (nums[i]-1!=i)):
                if(nums[i] != nums[nums[i]-1]):
                    temp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = temp
                    i-=1
            i+=1
        for i in range(len(nums)):
            if(i+1 != nums[i]):
                return i+1
        return (len(nums)+1)
        