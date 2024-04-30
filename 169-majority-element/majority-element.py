class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = [-1,-1]
        elements = dict()
        for e in nums:
            elements[e] = elements.get(e,0) + 1
            if(elements.get(e) > max[0]):
                max[0] = elements.get(e)
                max[1] = e
        return max[1]
