class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        output = []
        i = 0
        while i < (len(nums)-2):
            search = nums[i]*(-1)
            j = i+1
            k = len(nums)-1
            print(i)
            while(j != k):
                if(nums[j] + nums[k] > search):
                    k-=1
                    while(nums[k] == nums[k+1] and k!=j):
                        k-=1
                elif(nums[j] + nums[k] < search):
                    j+=1
                    while(nums[j-1] == nums[j] and k!=j):
                        j+=1
                else:
                    output.append([nums[i],nums[j],nums[k]])
                    j+=1
                    while(nums[j-1] == nums[j] and k!=j):
                        j+=1   
            i+=1
            while(nums[i-1] == nums[i] and i < (len(nums)-2)):
                i+=1                             
        return output
