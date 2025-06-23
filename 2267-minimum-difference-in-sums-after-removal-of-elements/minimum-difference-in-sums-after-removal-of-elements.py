from heapq import heappush, heappop, heapify

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        #Remove n elements
        #Split down the middle  minimize(sum(lefthalf) - sum(righthalf))

        #Goal:Minimize Left side, Maximize right side (Ascending order) remove n middle elements

        n = int(len(nums)/3)
        middle = nums[n:2*n]
        maxHeap = [-1 * x for x in nums[:n]]
        minHeap = nums[2*n:]

        #Identify maximum from first n nums
        heapify(maxHeap)

        #Identify minimum from last n nums
        heapify(minHeap)

        #Stores smallest possible prefix with n elements for nums[0...i] where i >= n and i < 2n
        prefixSums = [sum(nums[:n])] #Sum of (inclusive) nums[0:n-1]
        for i in range(n,2*n):
            tempSum = prefixSums[-1]
            if i >= n:
                #Might need to replace an element before calculating new prefix
                if (-1 * maxHeap[0]) > nums[i]:
                    #Remove from pastPrefix
                    removed = -1 * heappop(maxHeap)
                    tempSum += (nums[i] - removed)
                    heappush(maxHeap, (-1 * nums[i]))
            else:
                tempSum += nums[i]

            prefixSums.append(tempSum)

        #Stores largest possible suffix with n elements for nums[i...] where i > n and i <= 2n
        suffixSums = [sum(minHeap)] #Sum of (inclusive) nums[2n:3n-1]
        for i in range((2*n)-1,n-1, -1):
            tempSum = suffixSums[0]
            if i >= n:
                #Might need to replace an element before calculating new suffix
                if minHeap[0] < nums[i]:
                    #Remove from pastSuffix
                    removed = heappop(minHeap)
                    tempSum += (nums[i] - removed)
                    heappush(minHeap, nums[i])
            else:
                tempSum += nums[i]

            suffixSums.insert(0,tempSum)


        #Now for each combination of non-overlapping prefixes and suffixes,
        #Find the one with the minimum difference
        minDifference = float('inf')
        for p, s in zip(prefixSums, suffixSums):
            minDifference = min(minDifference, p - s)

        print(prefixSums)
        print(suffixSums)
        return minDifference


        #[16,46,43,41,42,14,36,    49,50,28,38,25,17,5,      18,11,14,21,23,39,23]
        #[46,43,42,41,36,16,14    49,50,28,38,25,17,5,      11,14,18,21,23,23,39,]
        

        





