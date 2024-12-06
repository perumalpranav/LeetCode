class Solution(object):
    def waysToMakeFair(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Basic Solution: (Brute Force)
        #Find even and odd sums for each element's left and right arrays (this was converted to  DP)
        #Use this to compute if array will be fair

        ways = 0
        n = len(nums) 

        #Each element of dp array will have (before,after) of each element
        T = [[(0,0),(0,0)]] * n
        initialSums = self.zeroOneSums(nums[1:])
        T[0] = [(0,0),initialSums]

        if (initialSums[0] == initialSums[1]):
            ways += 1

        #Recurrence Relation
        #IF i+1 is odd
            #i is even --> thus, before zeroSum should add i, and before oneSum should be the Same
            #T[i+1][0] = (T[i][0][0] + nums[i],T[i][0][1])
        #ELSE i+1 is even
            #i is odd --> thusm, before zeroSum stay same, and after zeroSum should add i
            #T[i+1][0] = (T[i][0][0],T[i][0][1] + nums[i])

        #After zeroSum should remove i+1, and after oneSum should be the Same
        #T[i+1][1] = (T[i][1][0] - nums[i+1],T[i][1][1])

        for i in range(1,n):
            evenSum = -100
            oddSum = -200  
            if i%2 == 0:
                #i is even
                T[i] = [(T[i-1][0][0],T[i-1][0][1] + nums[i-1]),(T[i-1][1][1],T[i-1][1][0] - nums[i])]
                evenSum = T[i][0][0] + T[i][1][0] #before(zero sum) + after(zero sum)
                oddSum = T[i][0][1] + T[i][1][1] #before(one sum) + after(one sum)
            else:
                #i is odd
                T[i] = [(T[i-1][0][0] + nums[i-1],T[i-1][0][1]),(T[i-1][1][1],T[i-1][1][0] - nums[i])]
                evenSum = T[i][0][0] + T[i][1][1] #before(zero sum) + after(one sum)
                oddSum = T[i][0][1] + T[i][1][0] #before(one sum) + after(zero sum)
            
            if (oddSum == evenSum):
                ways += 1
        
        return ways


    def zeroOneSums(self,arr):
        zeroSum = 0
        oneSum = 0
        for i in range(len(arr)):
            if i%2 == 0:
                zeroSum += arr[i]
            else:
                oneSum += arr[i]
        return (zeroSum,oneSum)