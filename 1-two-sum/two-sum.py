class Solution(object):
   def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortlist = sorted(nums)
        while(len(sortlist)>1):
            #min = sortlist[0]
            max = sortlist[len(sortlist)-1]
            if(sortlist[0] + max > target):
                sortlist.pop(len(sortlist)-1)
            elif(sortlist[0] + max < target):
                sortlist.pop(0)
            else:
                check = [False,False]
                rlist = []
                for i in range(len(nums)):
                    if(nums[i]==sortlist[0]):
                        rlist.append(i)
                    elif(nums[i]==max):
                        rlist.append(i)
                    if(len(rlist) == 2):
                        return rlist
        
        return [0,0]